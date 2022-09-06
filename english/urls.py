from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.eng, name='eng'),
    path('engcinema', views.engcinema, name='engcinema'),
    path('engwebseries', views.engwebseries, name='engwebseries'),
    
     
]
