from django.shortcuts import render, HttpResponse
from .models import  English, EngCinema, EngWebseries

# Create your views here.

def eng(request):
    movies = English.objects.all()
    return render(request,'pages/viewer.html', {'movies': movies})
    
def engcinema(request):
    cinemas = EngCinema.objects.all()
    return render(request,'pages/cinema.html', {'cinemas': cinemas})

def engwebseries(request):
    seriess = EngWebseries.objects.all()
    return render(request,'pages/series.html', {'seriess': seriess})
