from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.beng, name='beng'),

    path('bengcinema', views.bengcinema, name='bengcinema'),
    path('bengwebseries', views.bengwebseries, name='bengwebseries'),
    
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
