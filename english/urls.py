from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.eng, name='eng'),
    path('engcinema', views.engcinema, name='engcinema'),
    path('engwebseries', views.engwebseries, name='engwebseries'),
    
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
