from django.db import models
from decks.models import DeckModel

class CardModel(models.Model):
    card_id = models.IntegerField(primary_key=True)
    deck_id = models.ForeignKey(DeckModel, models.CASCADE)
    front_text = models.CharField(max_length=30)
    back_text = models.CharField(max_length=30)
    example_usage = models.TextField()