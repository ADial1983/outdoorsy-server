from django.db import models


class Image(models.Model):

    image = models.CharField(max_length=200)
