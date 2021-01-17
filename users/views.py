from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework.authtoken.models import Token

UserModel = get_user_model()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@login_required
def get_token(request):
    return HttpResponse(Token.objects.get(user=request.user).key)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'first_name', 'last_name')


class Register(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class PasswordTokenBackend(ModelBackend, TokenAuthentication):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Token Authentication
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2 and auth[0].lower() == self.keyword.lower().encode():
            try:
                token = auth[1].decode()
                return self.authenticate_credentials(token)[0]
            except UnicodeError:
                pass
        # Username authentication
        if username is None:
            username = kwargs.get('email')
        if username is None or password is None:
            return
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            try:
                user = UserModel.objects.get(email=username)
            except UserModel.DoesNotExist:
                return
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
