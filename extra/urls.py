from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.extra, name='extra'),
    path('extracinema/', views.extracinema, name='extracinema'),
    path('extrawebseries/', views.extrawebseries, name='extrawebseries'),
    
     
]
