from django.db import models
from SocialCred.models import UserInfo
from django.utils import timezone

# Create your models here.


class ChatBox(models.Model):

    sender = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="msgsender")
    receiver = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="mesreciever")
    message = models.TextField(default="")
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):

        return self.message