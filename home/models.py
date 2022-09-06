from django.db import models

# Create your models here.

class Home(models.Model):
    types = models.CharField(max_length=20, default="Cinema")
    ribbon = models.CharField(max_length=20, default="", blank="True")
    name = models.CharField(max_length=40, default="")
    lang = models.CharField(max_length=20, default="Bengali")
    poster = models.ImageField(upload_to='poster/home/' , default="") 
#    will be same for everywhere.
    quality = models.CharField(max_length=20, default="2160 FHD")
    spclnks = models.CharField(max_length=100, blank=True, default="#")
    price = models.CharField(max_length=20, default="Free")
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    hero = models.CharField(max_length=20, default="", blank=True)
    heroine = models.CharField(max_length=20, default="", blank=True)  
    about = models.CharField(max_length=200, default="Nothing Updated Yet", blank=True)
#    [ terabox link direct connect to video player ]
    watch = models.CharField(max_length=20, blank=True , default="")
    embededlink = models.CharField(max_length=500, default="#")
#  just type bengcinema or bengwebseries

    def __str__(self):
    	return self.name
