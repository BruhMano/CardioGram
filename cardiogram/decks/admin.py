from django.contrib import admin
from .models import Deck

class DeckAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields': ['name', 'description']})]

    list_display = ['id', 'name', 'description']

    search_fields = ['name']

admin.site.register(Deck, DeckAdmin)
