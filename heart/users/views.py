from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from . forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('login')
        else:
            messages.error(request, f'Errors')
            #return redirect('register')
    else:
        form = UserRegisterForm()

    return render(request,'users/register.html',{'form':form,'nbar': 'register'})


def login(request):    
    if request.user.is_authenticated:
        return redirect('home')

@login_required()
def profile(request):
    return render(request,'users/profile.html',{'nbar': 'profile'})

def aboutus(request):
    #return HttpResponse("<h1>Home</h1>")
    return render(request, 'users/aboutus.html',{'nbar': 'aboutus'})

def contactus(request):
    return render(request, 'users/contactus.html',{'nbar':'contactus'})