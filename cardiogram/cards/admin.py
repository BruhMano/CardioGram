from django.contrib import admin
from .models import Card

class CardAdmin(admin.ModelAdmin):
    fieldsets = [(
            None,
            {
                'fields': [ 'deck_id', 'front_text', 'back_text', 'example_usage']
            }
        )]

admin.site.register(Card, CardAdmin)
