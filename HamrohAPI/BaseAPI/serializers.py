from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ['LocationName', 'Country']