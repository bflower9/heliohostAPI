from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')
    search_fields = ('id', 'username', 'email', 'first_name', 'last_name')


admin.site.register(User, UserAdmin)
