from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    timestamp = models.DateTimeField(
        default=timezone.now(), 
        blank=True
    )
    