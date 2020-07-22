from django.urls import path, include
from . import views
app_name = 'Blog'
urlpatterns = [

    path('sblog/<int:id>', views.sblog, name="sblog"),
    path('bloglist', views.bloglist, name="bloglist"),
    path('addblog', views.addblog, name="addblog"),
    path('myblog', views.myblog, name="myblog")
]