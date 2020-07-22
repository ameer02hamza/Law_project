from django.urls import path, include
from . import views
app_name = 'Appointment'
urlpatterns = [
path('aform/<int:id>', views.aform, name="Appointform"),
path('status', views.status, name="status"),
path('test', views.test, name="st"),
path('requests', views.apprequest, name="arequests"),
path('reject/<int:id>', views.reject, name="reject"),
path('confirm/<int:id>', views.confirmed, name="confirm"),
path('notiajax', views.appointnoti, name="notiajax"),
path("notistatus/<int:id>", views.notiend, name="notiend")
]