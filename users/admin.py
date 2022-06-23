from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserRegistration
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = UserRegistration
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email']


admin.site.register(CustomUser, CustomUserAdmin)

