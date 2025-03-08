from django.contrib import admin
from .models import Progress
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class CustomUserAdmin(UserAdmin):

    list_display = ('username', 'email', 'password', 'first_name', 'last_name', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

class ProgressAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields': ['user_id', 'card_id','attempts', 'successful_attempts']})]

    list_display = ['progress_id', 'user_id', 'card_id','attempts', 'successful_attempts']

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Progress, ProgressAdmin)

