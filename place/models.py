from django.db import models
from city.models import City
# from sub_time.models import Sub_time

class Place(models.Model):
    # submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=60, null=True)
    adress = models.CharField(max_length=60, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.place_name} {self.city} {self.adress}'