from django.shortcuts import render, HttpResponse
from .models import Requestmovie
# from django.urls import Path , include
from .import models



# Create your views here.

def requestmovie(request):
    if request.method=='POST':
   	 reqname = request.POST['reqname']
   	 reqemail = request.POST['reqemail']   	 
   	 reqmovie = request.POST['reqmovie']
   	 filmname = request.POST['filmname']
   	 explnmovie = request.POST['explnmovie']

   	 
   	 requestmovie = Requestmovie(reqname=reqname, reqemail=reqemail, filmname=filmname, explnmovie=explnmovie)
   	 requestmovie.save()

    return render(request,'pages/reqMovie.html')
 
