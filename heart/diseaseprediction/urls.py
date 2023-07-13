from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('predictions/', views.predictions,name='predictions'),
    path('makeprediction/', views.makeprediction,name='makeprediction'),
    path('result/', views.result,name='result'),

]