from django.db import models
from django.utils import timezone


class Users(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    time_create = models.DateTimeField(default=timezone.now)

