from django.core.cache import cache
from django.db.models import Avg
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


def parse_bool(value):
    if value is None:
        return None
    value = str(value).lower()
    if value in ["true", "1"]:
        return True
    if value in ["false", "0"]:
        return False
    return None


class AuthorListCreateView(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def get_queryset(self):
        queryset = Author.objects.all()
        params = self.request.query_params

        if params.get("country"):
            queryset = queryset.filter(country__iexact=params.get("country"))

        if params.get("birth_year"):
            try:
                queryset = queryset.filter(birth_date__year=int(params.get("birth_year")))
            except:
                pass

        return queryset


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookListCreateView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.select_related("author").all()

    def get_queryset(self):
        queryset = Book.objects.select_related("author").all()
        params = self.request.query_params

        if params.get("author_id"):
            try:
                queryset = queryset.filter(author_id=int(params.get("author_id")))
            except:
                pass

        available = parse_bool(params.get("is_available"))
        if available is not None:
            queryset = queryset.filter(is_available=available)

        if params.get("min_price"):
            queryset = queryset.filter(price__gte=params.get("min_price"))

        if params.get("max_price"):
            queryset = queryset.filter(price__lte=params.get("max_price"))

        if params.get("year"):
            try:
                queryset = queryset.filter(published_date__year=int(params.get("year")))
            except:
                pass

        if params.get("search"):
            queryset = queryset.filter(title__icontains=params.get("search"))

        return queryset


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookStatsView(APIView):
    def get(self, request):
        return Response({
            "total_books": Book.objects.count(),
            "available_books": Book.objects.filter(is_available=True).count(),
            "average_price": Book.objects.aggregate(avg=Avg("price"))["avg"] or 0
        })