from django.contrib.auth import get_user_model 
from rest_framework import serializers
from .models import userprofile
import json


class UserSerializer(serializers.ModelSerializer): # new
    queryset = userprofile.objects.all()
    class Meta:
        model = userprofile
        fields = ['consumer_id','firstName','lastName','major','track','totalUnits','degreeProgress', 'transcript_json']
