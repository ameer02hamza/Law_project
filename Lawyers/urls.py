from django.urls import path, include
from . import views
app_name = 'lawyer'
urlpatterns = [
path("list", views.listing, name="Lawyerlist"),
path(r"slaw/<int:id>", views.slisting, name="SLawyerlist"),
]