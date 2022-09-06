from django.shortcuts import render, HttpResponse
from .models import Hindi, HinCinema, HinWebseries

# Create your views here.

def hin(request):
    movies = Hindi.objects.all()
    return render(request,'pages/viewer.html', {'movies': movies})
 
def hincinema(request):
    cinemas = HinCinema.objects.all()
    return render(request,'pages/cinema.html', {'cinemas': cinemas})

def hinwebseries(request):
    seriess = HinWebseries.objects.all()
    return render(request,'pages/series.html', {'seriess': seriess})
