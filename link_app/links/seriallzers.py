from django.shortcuts import render
from rest_framework import serializers

from .models import Links
from users.models import Users


class LinkApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = "__all__"