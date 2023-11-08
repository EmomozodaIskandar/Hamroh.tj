from django.shortcuts import render, HttpResponse
from rest_framework import generics
from .models import *
from .serializers import *
from django.forms.models import model_to_dict

class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class userCreationAPIView(generics.CreateAPIView, generics.ListAPIView):
    queryset = User.object.all()
    serializer_class = UserSerializer

class LocationsAPIVIew(generics.ListAPIView):
    queryset = Locations.objects.all()
    serializer_class = LocationSerializer