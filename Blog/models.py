from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime

class AddBlog(models.Model):
    btitle = models.CharField(max_length=120, default="")
    btext = models.TextField(default=" ")
    bpic = models.ImageField(upload_to="Blog/")
    btime = models.TimeField(default=timezone.now)
    bdate = models.DateField(default=timezone.now)
    postedby = models.ForeignKey(User, on_delete=models.CASCADE)
