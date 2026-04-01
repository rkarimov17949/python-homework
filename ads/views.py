from django.db.models import Q, Count
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Advertisement
from .serializers import AdvertisementSerializer


class AdvertisementListCreateView(generics.ListCreateAPIView):
    serializer_class = AdvertisementSerializer

    def get_queryset(self):
        queryset = Advertisement.objects.all()

        status_param = self.request.query_params.get("status")
        min_price = self.request.query_params.get("min_price")
        max_price = self.request.query_params.get("max_price")
        search = self.request.query_params.get("search")

        if status_param:
            queryset = queryset.filter(status=status_param)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        if search:
            queryset = queryset.filter(title__icontains=search)

        return queryset


class AdvertisementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    def perform_update(self, serializer):
        ad = self.get_object()
        if ad.status == "EXPIRED":
            raise ValueError("Expired advertisement cannot be modified.")
        serializer.save()


class ApproveAdvertisementView(APIView):
    def post(self, request, pk):
        try:
            ad = Advertisement.objects.get(pk=pk)
        except Advertisement.DoesNotExist:
            return Response({"error": "Advertisement not found"}, status=404)

        ad.approve()
        return Response({"message": "Approved"})


class RejectAdvertisementView(APIView):
    def post(self, request, pk):
        try:
            ad = Advertisement.objects.get(pk=pk)
        except Advertisement.DoesNotExist:
            return Response({"error": "Advertisement not found"}, status=404)

        ad.status = "REJECTED"
        ad.save()
        return Response({"message": "Rejected"})


class StatsView(APIView):
    def get(self, request):
        total_ads = Advertisement.objects.count()
        approved_ads = Advertisement.objects.filter(status="APPROVED").count()
        expired_ads = Advertisement.objects.filter(status="EXPIRED").count()
        rejected_ads = Advertisement.objects.filter(status="REJECTED").count()

        return Response({
            "total_ads": total_ads,
            "approved_ads": approved_ads,
            "expired_ads": expired_ads,
            "rejected_ads": rejected_ads,
        })
