from django_use_email_as_username.models import BaseUser, BaseUserManager
from django.db import models

class User(BaseUser):
    object = BaseUserManager()

class Locations(models.Model):
    LocationName = models.CharField(max_length=128)
    Country = models.CharField(max_length=64, default="Tajikistan")

    def __str__(self):
        return self.LocationName + "," + self.Country
