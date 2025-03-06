from django.contrib import admin
from .models import CardModel

class CardAdmin(admin.ModelAdmin):
    fields = ['card_id', 'deck_id', 'front_text', 'back_text', 'description']

admin.site.register(CardModel, CardAdmin)
