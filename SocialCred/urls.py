from django.urls import path, include
from . import views
app_name = "SocialCred"
urlpatterns = [
    path("", views.login, name="login"),
    path("signup/", views.signup, name="register"),
    path(r'logout', views.logout, name='logout'),
    path(r'master', views.masterlaw, name='master'),

]