from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from faceModel.models import FaceModelSerializer, FaceModels, IsOwner


class FaceModelsViewSet(viewsets.ModelViewSet):
    @action(detail=False)
    def check(self, request, *args, **kwargs):
        if request.GET.get('name'):
            try:
                FaceModels.objects.get(name=request.GET.get('name'))
                return Response({"status": True})
            except FaceModels.DoesNotExist:
                pass
        return Response({"status": False})

    lookup_field = 'name'
    queryset = FaceModels.objects.all()
    serializer_class = FaceModelSerializer
    permission_classes = [IsOwner]
