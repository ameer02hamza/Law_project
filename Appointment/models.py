from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class AppointmentForm(models.Model):

    Name = models.CharField(max_length=50)
    email = models.EmailField(default="")
    Phone_no = models.BigIntegerField( default=0)
    case_details = models.TextField(default="")
    adate = models.DateField(default=timezone.now)
    atime = models.TimeField(default=timezone.now)
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usernames')
    lawyer = models.ManyToManyField(User, related_name="lawyers", default=0)
    status = models.CharField(max_length=50, default="pending")

    def __str__(self):
        return self.Name

class notify(models.Model):
    msg = models.CharField(max_length=255, default="You have new Appointment Request")
    NfL = models.BooleanField(default=True)
    NfC = models.BooleanField(default=False)
    ndate =models.DateField(default=timezone.now)
    ntime = models.TimeField(default=timezone.now)
    frm = models.ForeignKey(AppointmentForm, on_delete=models.CASCADE)

    def __str__(self):
        return self.msg
