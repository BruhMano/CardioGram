from django.db import models
from decks.models import Deck

class Card(models.Model):
    deck = models.ForeignKey(Deck, models.CASCADE, null=False)
    front_text = models.CharField(max_length=30, unique=False, null=False)
    back_text = models.CharField(max_length=30,unique=False, null=False)
    example_usage = models.TextField(unique=True, null=True)

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

    def __str__(self):
        return self.front_text