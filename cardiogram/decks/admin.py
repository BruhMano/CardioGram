from django.contrib import admin
from .models import Deck

class DeckAdmin(admin.ModelAdmin):
    fieldsets = [(
            None,
            {
                'fields': ['deck_name', 'description']
            }
        )]
    list_display = ['deck_id', 'deck_name', 'description']

admin.site.register(Deck, DeckAdmin)
