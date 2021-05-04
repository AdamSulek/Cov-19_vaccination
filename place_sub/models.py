from django.db import models
from place.models import Place
from submission.models import Submission

class Place_sub(models.Model):
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE)
    sub_id = models.OneToOneField(Submission, on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    def __str__(self):
        return f'{self.place_id.city}, {self.place_id.place_name}, {self.date_time}'
