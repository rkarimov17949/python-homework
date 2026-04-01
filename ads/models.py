from django.db import models
from django.utils import timezone
from datetime import timedelta


class Advertisement(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('EXPIRED', 'Expired'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def approve(self):
        self.status = 'APPROVED'
        self.approved_at = timezone.now()
        self.expires_at = timezone.now() + timedelta(days=7)
        self.save()

    def __str__(self):
        return self.title