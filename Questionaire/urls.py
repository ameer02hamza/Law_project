from django.urls import path
from .views import (ArticleListView, AskQuestion)
# Questiondet, Questionupdate

app_name = "Questionaire"

urlpatterns = [
    path('det', ArticleListView.as_view(), name="lists"),
    path('askq', AskQuestion.as_view(), name="askq"),
    # path('det1', Questiondet.as_view(), name="l"),
    # path('<int:id>/update', Questionupdate.as_view(), name="l"),
]