from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.extra, name='extra'),
    path('extracinema/', views.extracinema, name='extracinema'),
    path('extrawebseries/', views.extrawebseries, name='extrawebseries'),
    
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
