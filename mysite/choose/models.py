from django.db import models
import datetime
from django.utils import timezone

class Venue(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    distance = models.CharField(max_length=200)
    selected = models.BooleanField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name
