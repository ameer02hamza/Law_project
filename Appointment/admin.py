from django.contrib import admin
from . models import AppointmentForm, notify
# Register your models here.
admin.site.register(AppointmentForm)
admin.site.register(notify)
