from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    profile_picture = models.ImageField(upload_to="UserInfo/")
    usrtype = models.BooleanField(default=False)
    address = models.CharField(max_length=255, default="")
    pno = models.BigIntegerField(default=0)
    description = models.TextField(default="")
    speciality = models.CharField(max_length=255, default="")
    usr = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.address

