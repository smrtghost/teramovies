from django.shortcuts import render, HttpResponse
#from django.contrib import messages
from home.models import Home
from bengali.models import Bengali, BengCinema, BengWebseries
from hindi.models import Hindi, HinCinema, HinWebseries
from english.models import English, EngCinema, EngWebseries

# Create your views here.

def home(request):
    movies = Home.objects.all()
    return render(request,'pages/index.html', {'movies': movies})
    


def about(request):
    return render(request,'pages/about.html')
 
def termsConditions(request):
	return render(request,'pages/termsConditions.html')
	
	
def legalRights(request):
	return render(request,'pages/legalRights.html')
	
	
def contributors(request):
	return render(request,'pages/contributors.html')

	
def search(request):
	#allMovie = movies.objects.all()
	search = request.GET['search']
	allBengali = "Bengali.objects.filter(title__icontains=search)" + "BengCinema.objects.filter(title__icontains=search)" + "BengWebseries.objects.filter(title__icontains=search)"
	allHindi = "Hindi.objects.filter(title__icontains=search)" + "HinCinema.objects.filter(title__icontains=search)" + "HinWebseries.objects.filter(title__icontains=search)"
	allEnglish = "English.objects.filter(title__icontains=search)" + "EngCinema.objects.filter(title__icontains=search)" + "EngWebseries.objects.filter(title__icontains=search)"
	
	allMovie = "allBengali" + "allHindi" + "allEnglish"
	
	params = "{'movies': movies}" + "{'seriess': seriess}" + "{'cinemas': cinemas}"
	
	return render(request,'pages/cinema.html', params)


