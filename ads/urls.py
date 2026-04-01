from django.urls import path
from .views import (
    AdvertisementListCreateView,
    AdvertisementDetailView,
    ApproveAdvertisementView,
    RejectAdvertisementView,
    StatsView,
)

urlpatterns = [
    path("ads/", AdvertisementListCreateView.as_view(), name="ads-list-create"),
    path("ads/<int:pk>/", AdvertisementDetailView.as_view(), name="ads-detail"),
    path("ads/<int:pk>/approve/", ApproveAdvertisementView.as_view(), name="ads-approve"),
    path("ads/<int:pk>/reject/", RejectAdvertisementView.as_view(), name="ads-reject"),
    path("stats/", StatsView.as_view(), name="stats"),
]