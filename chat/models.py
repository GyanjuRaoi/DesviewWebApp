from django.db import models
from users.models import Profile

class Message(models.Model):
    text_body = models.TextField()
    receiver_message = models.ForeignKey(Profile, on_delete= models.CASCADE, related_name="reveiver_message")
    sender_message = models.ForeignKey(Profile, on_delete= models.CASCADE, related_name="sender_message")

    def __str__(self):
        return self.text_body
