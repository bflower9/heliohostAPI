from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

urlpatterns = [
    path('', lambda: HttpResponse('Welcome to api.mahbd.heliohost.us')),
    path('admin/', admin.site.urls),
    path('face_models/', include('faceModel.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
