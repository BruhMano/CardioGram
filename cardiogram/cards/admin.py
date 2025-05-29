from django.contrib import admin
from .models import Card

class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'deck', 'front_text', 'back_text', 'example_usage')

    search_fields = ('front_text', 'back_text')

    fieldsets = (
        ('Content', {'fields': ['front_text', 'back_text', 'example_usage', 'deck']},),
        )

admin.site.register(Card, CardAdmin)
