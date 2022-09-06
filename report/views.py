from django.shortcuts import render, HttpResponse
from .models import Report
# from django.urls import Path , include
from .import models



# Create your views here.

def report(request):
    if request.method=='POST':
   	 repname = request.POST['repname']
   	 repemail = request.POST['repemail']   	 
   	 repissue = request.POST['repissue']
   	 replink = request.POST['replink']
   	 repmessage = request.POST['repmessage']
   	 
   	 report = Report(repname=repname, repemail=repemail, repissue=repissue, replink=replink,repmessage=repmessage)
   	 report.save()

    return render(request,'pages/reportMovie.html')
 


