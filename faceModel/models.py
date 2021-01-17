from django.db import models
from rest_framework import serializers
from rest_framework.permissions import BasePermission

from users.models import User


def add_user_in_serializer(self, attrs):
    if self.instance:
        pass
    else:
        if not attrs.get('user'):
            attrs['user'] = self.context['request'].user
    return attrs


class FaceModels(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    name = models.CharField(max_length=255, unique=True)
    data = models.JSONField(null=True)


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user.id == 2 or obj.user.id == request.user.id


class FaceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceModels
        fields = '__all__'

    def validate(self, attrs):
        if self.instance:
            pass
        else:
            attrs = add_user_in_serializer(self, attrs)
        return attrs
