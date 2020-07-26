from django.contrib import admin
from django.urls import path, include,re_path
from . import views
app_name = "ChatApp"
urlpatterns = [
    path("", views.chatbox, name="inbox"),
    re_path(r"^(?P<username>[\w.@+-]+)", views.send, name="send"),

]