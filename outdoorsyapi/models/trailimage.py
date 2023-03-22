from django.db import models

class TrailImage(models.Model):

    image = models.ForeignKey("Image", on_delete=models.CASCADE, related_name='image_for_trail')
    trail = models.ForeignKey("Trail", on_delete=models.CASCADE, related_name='trail_for_image')
