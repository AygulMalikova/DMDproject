from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    model = models.TextField(default="")
    amount_of_places = models.IntegerField(default=4)
    color = models.TextField(default="white")

    def __unicode__(self):
        return u"%s" % self.model
