from django.db import models
from core.models import AbstractTimeStampedModel


class Conversation(AbstractTimeStampedModel):

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        usernames = [user.username for user in self.participants.all()]
        return ", ".join(usernames)

    def count_messages(self):
        return self.messages.count()
    count_messages.short_description = "Number of Message(s)"

    def count_participants(self):
        return self.participants.count()
    count_participants.short_description = "Number of Participant(s)"


class Message(AbstractTimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey("users.User", related_name="messages", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversation", related_name="messages", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says ({self.message})"
