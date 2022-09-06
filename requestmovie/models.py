from django.db import models 
from django.urls import path, include


# Create your models here.

class Requestmovie(models.Model):
	slno = models.AutoField(primary_key=True)
	reqname = models.CharField(max_length=50)
	reqemail = models.EmailField(max_length=100)	
	reqmovie = models.TextField(max_length=50)
	filmname = models.CharField(max_length=50)	
	explnmovie = models.TextField(max_length=200)
	timeStamp = models.DateTimeField(auto_now_add=True, blank=True)


