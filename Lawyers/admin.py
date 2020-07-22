from django.contrib import admin
from . models import rating
# Register your models here.
class sadmin(admin.ModelAdmin):
    list_display = ('id','ratings','review','RoL', 'RC')
admin.site.register(rating, sadmin)
