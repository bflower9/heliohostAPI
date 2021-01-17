from django.db.models import Q
from rest_framework import viewsets

from faceModel.models import FaceModelSerializer, FaceModels


class FaceModelsViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return FaceModels.objects.filter(Q(user_id=2) | Q(user=self.request.user))
        return FaceModels.objects.filter(user_id=2)

    lookup_field = 'name'
    serializer_class = FaceModelSerializer
