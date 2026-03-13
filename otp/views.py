from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.mail import send_mail

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework_simplejwt.tokens import RefreshToken

from api.models import Item
from api.serializers import (
    ItemCreateSerializer,
    ItemListSerializer,
    ItemAdminUpdateSerializer,
)
import random
import string


def generate_otp():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


class RequestOTP(APIView):
    def post(self, request):
        email = request.data.get("email")

        if not email:
            return Response(
                {"error": "Email is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        existing_otp = cache.get(f"otp_{email}")
        if existing_otp:
            return Response(
                {"error": "OTP already sent. Wait until it expires."},
                status=status.HTTP_400_BAD_REQUEST
            )

        otp = generate_otp()
        cache.set(f"otp_{email}", otp, timeout=300)

        send_mail(
            subject="Your OTP Code",
            message=f"Your OTP is: {otp}",
            from_email="noreply@example.com",
            recipient_list=[email],
            fail_silently=True,
        )

        return Response(
            {
                "message": "OTP sent successfully",
                "otp": otp
            },
            status=status.HTTP_200_OK
        )


class VerifyOTP(APIView):
    def post(self, request):
        email = request.data.get("email")
        otp = request.data.get("otp")

        if not email or not otp:
            return Response(
                {"error": "Email and OTP are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        cached_otp = cache.get(f"otp_{email}")

        if not cached_otp:
            return Response(
                {"error": "OTP expired or not found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if cached_otp != otp:
            return Response(
                {"error": "Invalid OTP"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user, created = User.objects.get_or_create(
            username=email,
            defaults={"email": email}
        )

        if not user.email:
            user.email = email
            user.save()

        cache.delete(f"otp_{email}")

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "message": "OTP verified",
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            },
            status=status.HTTP_200_OK
        )


class ItemCreateView(generics.CreateAPIView):
    serializer_class = ItemCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class ApprovedItemsView(generics.ListAPIView):
    serializer_class = ItemListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Item.objects.filter(status="APPROVED").order_by("-created_at")


class MyItemsView(generics.ListAPIView):
    serializer_class = ItemListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['status', 'created_at']
    search_fields = ['title']

    def get_queryset(self):
        return Item.objects.filter(created_by=self.request.user).order_by("-created_at")


class ItemAdminUpdateView(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemAdminUpdateSerializer
    permission_classes = [permissions.IsAdminUser]