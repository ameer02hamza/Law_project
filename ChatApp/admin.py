from django.contrib import admin
from . models import ChatBox
# Register your models here.


class sadmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'message','datetime')


admin.site.register(ChatBox,sadmin)