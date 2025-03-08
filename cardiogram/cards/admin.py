from django.contrib import admin
from .models import Card

class CardAdmin(admin.ModelAdmin):
    list_display = ('deck_id', 'front_text', 'back_text', 'example_usage')

    search_fields = ('front_text', 'back_text')

    fieldsets = (
        ('Content', {'fields': ['front_text', 'back_text', 'example_usage']},),
        )

admin.site.register(Card, CardAdmin)
