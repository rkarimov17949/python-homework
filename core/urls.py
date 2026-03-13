"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from otp.views import (
    RequestOTP,
    VerifyOTP,
    ItemCreateView,
    ApprovedItemsView,
    MyItemsView,
    ItemAdminUpdateView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/send-otp/', RequestOTP.as_view()),
    path('auth/verify-otp/', VerifyOTP.as_view()),
    path('items/', ItemCreateView.as_view()),
    path('items/approved/', ApprovedItemsView.as_view()),
    path('items/my/', MyItemsView.as_view()),
    path('items/<int:pk>/status/', ItemAdminUpdateView.as_view()),
]