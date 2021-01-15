from django.contrib import admin

from faceModel.models import FaceModels


class FaceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'user__username', 'user__first_name', 'user__last_name')


admin.site.register(FaceModels, FaceAdmin)
