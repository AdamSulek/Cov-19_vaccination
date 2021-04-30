from django.db import models

# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length=60, null=False)

    def __str__(self):
        return f'{self.city_name}'
