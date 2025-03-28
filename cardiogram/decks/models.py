from django.db import models

class Deck(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    description = models.TextField(unique=True, null=True)

    class Meta:
        verbose_name = 'Колода'
        verbose_name_plural = 'Колоды'


    def __str__(self):
        return self.name
