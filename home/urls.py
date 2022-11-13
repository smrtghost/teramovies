from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contributors', views.contributors, name='contributors'),
    path('legalRights', views.legalRights, name='legalRights'),
    path('termsConditions', views.termsConditions, name='termsConditions'),
    path('search', views.search, name='search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
