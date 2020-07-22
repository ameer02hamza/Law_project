from django.urls import path
from . import views
app_name = 'Search'
urlpatterns = [
    path('searchlawyer', views.lawyer, name="searchlawyer"),
    path('searchblog', views.blog, name="searchblog"),
    path('lists', views.searchlaw, name="lawlists"),
    path('blogs', views.blores, name="bres"),
]