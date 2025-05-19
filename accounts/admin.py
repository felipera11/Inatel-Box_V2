# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

CustomUser = get_user_model()

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'email', 'is_staff')
