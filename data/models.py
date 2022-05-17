from operator import mod
from django.db import models
from django.contrib.auth import get_user_model 
# Create your models here.

class userprofile(models.Model):
    
    consumer =  models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    major = models.CharField(max_length=100)
    track = models.CharField(max_length=400)
    totalUnits = models.IntegerField(default=0)
    degreeProgress = models.IntegerField(default=0)
    transcript_json = models.JSONField()