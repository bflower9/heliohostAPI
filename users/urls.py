from django.http import JsonResponse
from django.urls import path, include

from users import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.Register.as_view(), name='register'),
    path('get-token/', views.get_token),
    path('is_logged/', lambda x: JsonResponse({'result': x.user.is_authenticated}))
]
