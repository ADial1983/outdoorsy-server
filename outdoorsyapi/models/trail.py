from django.db import models


class Trail(models.Model):

    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    length = models.FloatField()
