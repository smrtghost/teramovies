from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.hin, name='hin'),
    path('hincinema', views.hincinema, name='hincinema'),
    path('hinwebseries', views.hinwebseries, name='hinwebseries'),
    
     
]
