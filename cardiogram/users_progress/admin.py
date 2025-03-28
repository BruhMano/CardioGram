from django.contrib import admin
from .models import Progress
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

class CustomUserAdmin(UserAdmin):

    list_display = ('username', 'email', 'password', 'first_name', 'last_name', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

class ProgressAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields': ['user', 'card','attempts', 'successful_attempts']})]

    list_display = ['id', 'user', 'card','attempts', 'successful_attempts']

admin.site.unregister(get_user_model())
admin.site.unregister(Group)
admin.site.register(get_user_model(), CustomUserAdmin)
admin.site.register(Progress, ProgressAdmin)

