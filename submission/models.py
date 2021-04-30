from django.db import models
from account.models import Account

class Submission(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    dialisis = models.BooleanField(default=False)
    cancers = models.BooleanField(default=False)
    transplant = models.BooleanField(default=False)
    thrombosis = models.BooleanField(default=False)
    chronic = models.BooleanField(default=False)
    drugs = models.CharField(max_length=100, null=True, blank=True)
    additional_question = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}'
