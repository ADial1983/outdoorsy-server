from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer_of_review')
    trail = models.ForeignKey("Trail", on_delete=models.CASCADE, related_name='trail_of_review')
    review = models.CharField(max_length=1000, null=True)

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value
    