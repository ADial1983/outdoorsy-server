from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Rating(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rater_of_rating')
    trail = models.ForeignKey("Trail", on_delete=models.CASCADE, related_name='trail_of_rating')
    parking = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=False)
    bathroom = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=False)
    width = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=False)
    clear = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=False)
    steep = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=False)
