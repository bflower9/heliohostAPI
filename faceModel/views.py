# from django.db.models import Q
# from rest_framework import viewsets
#
# from faceModel.models import FaceModelSerializer, FaceModels
#
#
# class FaceModelsViewSet(viewsets.ModelViewSet):
#     def get_queryset(self):
#         return FaceModels.objects.filter(Q(user=None) | Q(user=self.request.user))
#
#     lookup_field = 'name'
#     serializer_class = FaceModelSerializer
