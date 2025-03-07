from django.contrib import admin
from .models import Progress

class ProgressAdmin(admin.ModelAdmin):
    fieldsets = [(
            None,
            {
                'fields': ['user_id', 'card_id','attempts', 'successful_attempts']
            }
        )]

admin.site.register(Progress, ProgressAdmin)
