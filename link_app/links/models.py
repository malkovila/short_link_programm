from django.db import models

from users.models import Users


class Links(models.Model):
    original_url = models.CharField(max_length=255)
    short_url = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(null=True, blank=True)
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)


