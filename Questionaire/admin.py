from django.contrib import admin
from .models import Question


class sadmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'question',  'ptime', 'uprof')


admin.site.register(Question, sadmin)