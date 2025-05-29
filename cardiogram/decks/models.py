from django.db import models
from django.conf import settings

class Deck(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    description = models.TextField(unique=True, null=True)
    cover = models.ImageField(upload_to='decks/')

    class Meta:
        verbose_name = 'Колода'
        verbose_name_plural = 'Колоды'


    def __str__(self):
        return self.name
