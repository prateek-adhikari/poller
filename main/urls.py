from django.urls import path
from main.views import Index,Question
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('question/<slug>', login_required(Question.as_view()), name="question")
]