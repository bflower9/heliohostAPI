from django.db import models
from django_jsonfield_backport.models import JSONField
from rest_framework import serializers

from users.models import User


class FaceModels(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    data = JSONField(null=True)


class FaceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceModels
        fields = '__all__'
