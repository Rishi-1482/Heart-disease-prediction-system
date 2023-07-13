from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
from sklearn import *
import joblib
from . forms import Prediction
from diseaseprediction.forms import PredictionForm
from django.contrib import messages


def home(request):
    return render(request, 'diseaseprediction/home.html',{'nbar': 'home'})


def result(request):
    return render(request, 'diseaseprediction/result.html')


def predictions(request):
    plist = Prediction.objects.filter(user=request.user).order_by('created_at').reverse() #python object based query
    plist_count = plist.count #for finding how many records are inserted
    return render(request,'diseaseprediction/predictions.html',{'plist':plist,'plist_count':plist_count,'nbar': 'predictions'})


def makeprediction(request):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        
        model = joblib.load('final_model.sav')
        lst = []

        lst.append(int(request.POST.get('age')))
        lst.append(int(request.POST.get('sex')))
        lst.append(int(request.POST.get('cp')))
        lst.append(int(request.POST.get('trestbps')))
        lst.append(int(request.POST.get('chol')))
        lst.append(int(request.POST.get('fbs')))
        lst.append(int(request.POST.get('restecg')))
        lst.append(int(request.POST.get('thalach')))
        lst.append(int(request.POST.get('exang')))
        lst.append(float(request.POST.get('oldpeak')))
        lst.append(int(request.POST.get('slope')))
        lst.append(int(request.POST.get('ca')))
        lst.append(int(request.POST.get('thal')))

        # print(lst)
        lst_array = np.asarray(lst)
        lst_reshaped = lst_array.reshape(1,-1)
        ans = model.predict(lst_reshaped)
        message = ''

        if ans[0] == 0:
            message = "yes"
        
        elif ans[0] == 1:
            message = "no"
        new_request = request.POST.copy()
        new_request.update({'result': ans[0]})
    
        form = PredictionForm(new_request)
        # print(form)
        #current_user = request.user
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return render(request, 'diseaseprediction/result.html', {'message' : message})

            # messages.success(request, f'Prediction was created successfully')
            # return redirect('predictions') 
        else:
            messages.error(request, {'form':form})
            #return redirect('register')
    else:
        form = PredictionForm()

    return render(request, 'diseaseprediction/makeprediction.html',{'nbar': 'predictions'})