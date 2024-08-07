from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'name', 'is_staff', 'is_superuser']
    search_fields = ['email', 'name']
    ordering = ['email']
