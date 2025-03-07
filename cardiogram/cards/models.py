from django.db import models
from decks.models import Deck

class Card(models.Model):
    card_id = models.AutoField(primary_key=True)
    deck_id = models.ForeignKey(Deck, models.CASCADE)
    front_text = models.CharField(max_length=30)
    back_text = models.CharField(max_length=30)
    example_usage = models.TextField()