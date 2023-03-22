from django.db import models

class RatingReview(models.Model):

    rating = models.ForeignKey("Rating", on_delete=models.CASCADE, related_name='rating_for_review')
    review = models.ForeignKey("Review", on_delete=models.CASCADE, related_name='review_for_rating')

  