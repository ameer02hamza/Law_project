from django.db import models
from django.contrib.auth.models import User
from SocialCred.models import UserInfo
from django.utils import timezone
from django.urls import reverse


class Question(models.Model):

    title = models.CharField(max_length=50, default="")
    question = models.TextField(default="")
    ptime = models.TimeField(default=timezone.now)
    pdate = models.DateField(default=timezone.now)
    uprof = models.ForeignKey(UserInfo, on_delete=models.CASCADE)