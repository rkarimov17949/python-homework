from django.utils import timezone
from celery import shared_task
from .models import Advertisement


@shared_task
def expire_ads():
    ads = Advertisement.objects.filter(status="APPROVED", expires_at__lt=timezone.now())
    count = ads.update(status="EXPIRED")
    return f"{count} ads expired."