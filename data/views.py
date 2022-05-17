from django.shortcuts import render
from rest_framework.views import APIView
from .models import userprofile
from .serializers import UserSerializer
from rest_framework import generics, permissions, serializers, status
import json

# Create your views here.
class transcriptUploadView(APIView):
    def post(self, request, format=None):
        pass

class createView(generics.CreateAPIView):
    queryset = userprofile.objects.all()
    serializer_class = UserSerializer

class updateView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = userprofile.objects.all()
    #permission_classes = (IsConsumer,) Once we add permissions
    serializer_class = UserSerializer