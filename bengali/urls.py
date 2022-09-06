from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.beng, name='beng'),

    path('bengcinema', views.bengcinema, name='bengcinema'),
    path('bengwebseries', views.bengwebseries, name='bengwebseries'),
    
     
]
