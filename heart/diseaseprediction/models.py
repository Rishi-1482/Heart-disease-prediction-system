from django.db import models
from django.conf import settings
from django.contrib.auth.models import User 
# Create your models here.


class Prediction(models.Model):
    age = models.PositiveIntegerField()
    sex = models.PositiveIntegerField()
    cp = models.PositiveIntegerField()
    trestbps = models.PositiveIntegerField()
    chol = models.PositiveIntegerField()
    fbs = models.PositiveIntegerField()
    restecg = models.PositiveIntegerField()
    thalach = models.PositiveIntegerField()
    exang = models.PositiveIntegerField()
    oldpeak = models.FloatField()
    slope = models.PositiveIntegerField()
    ca = models.PositiveIntegerField()
    thal = models.PositiveIntegerField()
    result = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)



    