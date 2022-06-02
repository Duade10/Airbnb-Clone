from django.db import models
from core.models import AbstractTimeStampedModel

# REVIEW MODEL DEFINITION
class Review(AbstractTimeStampedModel):
    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    cleanliness = models.IntegerField()
    user = models.ForeignKey("users.User", related_name="reviews", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", related_name="reviews", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} | {self.user.username}"

    def rating_average(self):
        avg = (self.accuracy + self.communication + self.location + self.check_in + self.value + self.cleanliness) / 6
        return round(avg, 2)
