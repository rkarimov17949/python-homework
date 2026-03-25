from django.urls import path
from .views import AuthorListCreateView, AuthorDetailView, BookListCreateView, BookDetailView, BookStatsView

urlpatterns = [
    path("authors/", AuthorListCreateView.as_view()),
    path("authors/<int:pk>/", AuthorDetailView.as_view()),
    path("books/", BookListCreateView.as_view()),
    path("books/<int:pk>/", BookDetailView.as_view()),
    path("books/stats/", BookStatsView.as_view()),
]