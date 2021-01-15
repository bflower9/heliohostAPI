from django.db import models
from rest_framework import serializers

from users.models import User


class FaceModels(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    data = models.JSONField(null=True)


class FaceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceModels
        fields = '__all__'
