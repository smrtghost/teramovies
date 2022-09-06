from django.contrib import admin
from django.urls import path
from . import views





urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contributors', views.contributors, name='contributors'),
    path('legalRights', views.legalRights, name='legalRights'),
    path('termsConditions', views.termsConditions, name='termsConditions'),
    path('search', views.search, name='search'),

]
