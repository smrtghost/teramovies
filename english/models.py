from django.db import models

# Create your models here.

class English(models.Model):
    types = models.CharField(max_length=20, default="Web Series")
    ribbon = models.CharField(max_length=20, default="", blank="True")
    name = models.CharField(max_length=40, default="")
    lang = models.CharField(max_length=20, default="English")
    poster = models.ImageField(upload_to='poster/english/all/', default="") 
#    will be same for everywhere.
    quality = models.CharField(max_length=20, default="4K UHD")
    spclnks = models.CharField(max_length=100, blank=True, default="#")
    price = models.CharField(max_length=20, default="Free")
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    hero = models.CharField(max_length=20, default="", blank=True)
    heroine = models.CharField(max_length=20, default="", blank=True)  
    about = models.CharField(max_length=200, default="Nothing Updated Yet", blank=True)
#    [ terabox link direct connect to video player ]
    watch = models.CharField(max_length=20, blank=True, default="engcinema/engwebseries")
    embededlink = models.CharField(max_length=500, default="#", blank=True)
#  just type engcinema or engwebseries
    def __str__(self):
    	return self.name
  


class EngCinema(models.Model):
    types = models.CharField(max_length=20, default="Cinema")
    ribbon = models.CharField(max_length=20, default="", blank="True")
    name = models.CharField(max_length=40, default="")
    lang = models.CharField(max_length=20, default="Bengali")
    poster = models.ImageField(upload_to='poster/english/cinema/', default="") 
#    will be same for everywhere.
    quality = models.CharField(max_length=20, default="HD 1080")
    spclnks = models.CharField(max_length=100, blank=True, default="#")
    price = models.CharField(max_length=20, default="Free")
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    hero = models.CharField(max_length=20, default="", blank=True)
    heroine = models.CharField(max_length=20, default="", blank=True)  
    about = models.CharField(max_length=200, default="Nothing Updated Yet", blank=True)
#    [ terabox link direct connect to video player ]
    watch = models.CharField(max_length=20, blank=True, default="engcinema")
    embededlink = models.CharField(max_length=500, default="#", blank=True)
    def __str__(self):
    	return self.name


class EngWebseries(models.Model):
    types = models.CharField(max_length=20, default="WebSeries")
    ribbon = models.CharField(max_length=20, default="", blank="True")
    name = models.CharField(max_length=40, default="")
    lang = models.CharField(max_length=20, default="English")
    poster = models.ImageField(upload_to='poster/english/webseries/', default="") 
#    will be same for everywhere.
    quality = models.CharField(max_length=20, default="HD 1080")
    spclnks = models.CharField(max_length=100, blank=True, default="#")
    price = models.CharField(max_length=20, default="Free")
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    hero = models.CharField(max_length=20, default="", blank=True)
    heroine = models.CharField(max_length=20, default="", blank=True)  
    about = models.CharField(max_length=200, default="Nothing Updated Yet", blank=True)
#    [ terabox link direct connect to video player ]
    watch = models.CharField(max_length=20, blank=True, default="engwebseries")
    embededlink = models.CharField(max_length=500, default="#", blank=True)
    def __str__(self):
    	return self.name


