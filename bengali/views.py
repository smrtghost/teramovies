from django.shortcuts import render, HttpResponse
from .models import Bengali, BengCinema , BengWebseries

# Create your views here.

def beng(request):
    movies = Bengali.objects.all()
    return render(request,'pages/viewer.html', {'movies': movies})
   
 
def bengcinema(request):
    cinemas = BengCinema.objects.all()
    return render(request,'pages/cinema.html', {'cinemas': cinemas})



def bengwebseries(request):
    seriess = BengWebseries.objects.all()
    return render(request,'pages/series.html', {'seriess': seriess})

