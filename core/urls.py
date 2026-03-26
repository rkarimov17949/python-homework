from django.urls import path
from .views import BookStatsView

urlpatterns = [
    path("books/stats/", BookStatsView.as_view()),
]