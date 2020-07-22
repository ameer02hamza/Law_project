from django.contrib import admin
from .models import UserInfo

# Register your models here.
class sadmin(admin.ModelAdmin):
    list_display = ('usrtype','address','speciality', 'usr')

admin.site.register(UserInfo,sadmin)
