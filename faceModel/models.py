from django.db import models
from django_jsonfield_backport.models import JSONField
from rest_framework import serializers

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
    name = models.CharField(max_length=255)
    data = JSONField(null=True)


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
