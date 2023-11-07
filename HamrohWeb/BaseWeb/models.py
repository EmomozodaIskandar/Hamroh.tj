from django.db import models

# Create your models here.
class Locations(models.Model):
    LocationName = models.CharField(max_length=128)
    Country = models.CharField(max_length=64, default="Tajikistan")

    def __str__(self):
        return self.LocationName + "," + self.Country

