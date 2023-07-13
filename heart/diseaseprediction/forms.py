from django import forms
from diseaseprediction.models import Prediction
from diseaseprediction.models import User


class PredictionForm(forms.ModelForm):    
    class Meta:
        model = Prediction
        fields = ["age", "sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal","result"]

										