from django.shortcuts import render, HttpResponse

# Create your views here.

def extra(request):
    return render(request,'test.html')
 
def extracinema(request):
	return render(request,'test.html')

def extrawebseries(request):
	return render(request,'test.html')
