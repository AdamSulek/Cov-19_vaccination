from django.db import models
from city.models import City

class Place(models.Model):
    place_name = models.CharField(max_length=60, null=True)
    adress = models.CharField(max_length=60, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    website = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.city}, {self.adress}, {self.place_name}'
