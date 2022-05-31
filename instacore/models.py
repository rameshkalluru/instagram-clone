
from distutils.command.upload import upload
from time import monotonic
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save, post_delete
from django.utils.text import slugify



# Create your models here.
class Post(models.Model):
    image=models.FileField(upload_to='posts')
    caption=models.CharField(max_length=254, null=True)
    likes=models.ManyToManyField(User,default=None,blank=True)
  

    def __str__(self):
        return str(self.caption)
    

    def total_likes(self):
        return self.likes.count()

class Reel(models.Model):
    reel=models.FileField(upload_to='reels')
    caption=models.CharField(max_length=254,null=True)
   
    

    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):  
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=254,blank=True)
    bio=models.TextField( blank=True)
    photo=models.ImageField(upload_to='profile pics',null=True)
    followers = models.ManyToManyField(User,related_name="followers",blank=True)
    followings = models.ManyToManyField(User,related_name="followings",blank=True)
