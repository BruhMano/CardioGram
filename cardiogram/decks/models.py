from django.db import models

class Deck(models.Model):
    deck_id = models.AutoField(primary_key=True)
    deck_name = models.CharField(max_length=100)
    description = models.TextField()
