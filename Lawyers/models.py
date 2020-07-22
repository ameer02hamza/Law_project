from django.db import models
from django.contrib.auth.models import User

class rating(models.Model):

    ratings = models.DecimalField(max_digits=2, default=0.0, decimal_places=1)
    review = models.TextField()
    RoL = models.ForeignKey(User, on_delete=models.CASCADE)
    RC = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Rclients")

    def __str__(self):
        return self.review
