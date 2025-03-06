from django.db import models

class DeckModel(models.Model):
    deck_id = models.IntegerField(primary_key=True)
    deck_name = models.CharField(max_length=100)
    description = models.TextField()
