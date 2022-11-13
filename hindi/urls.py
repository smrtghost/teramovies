from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.hin, name='hin'),
    path('hincinema', views.hincinema, name='hincinema'),
    path('hinwebseries', views.hinwebseries, name='hinwebseries'),
    
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
