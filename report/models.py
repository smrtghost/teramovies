from django.db import models 
from django.urls import path, include


# Create your models here.

class Report(models.Model):
	slno = models.AutoField(primary_key=True)
	repname = models.CharField(max_length=50)
	repemail = models.EmailField(max_length=100)	
	repissue = models.TextField(max_length=50)
	replink = models.CharField(max_length=50)	
	repmessage = models.TextField(max_length=200)
	timeStamp = models.DateTimeField(auto_now_add=True, blank=True)


