from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Declear Variable that should match refferel id

refId = "FreeForAll"

# Create your views here.
    

    
def signup(request):

    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        secret = request.POST['secret']
        if refId == secret:
            pass
        else:
            return redirect('/accounts/signup') 
        
        
        if password==password:
            if User.objects.filter(username=username).exists():
                print("username already taken")
           
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('/accounts/signin')
    else:
       return render(request, "pages/signup.html") 
    return render(request, "pages/signup.html")
    
def signin(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "logged in successfully")
            return redirect("/")
        else:
            messages.error(request, 'invalid creadentials')
            return redirect('/accounts/signin')
    else:
        return render(request, 'pages/signin.html')
    return render(request, 'pages/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "logged out successfully")

    return redirect("/accounts/signin")
        
