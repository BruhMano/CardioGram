from django.db import models
from cards.models import Card
from django.contrib.auth import get_user_model

class Progress(models.Model):
    user = models.ForeignKey(get_user_model(), models.CASCADE, null=False)
    card = models.ForeignKey(Card, models.CASCADE, null=False)
    attempts = models.IntegerField()
    successful_attempts = models.IntegerField()

    class Meta:
        verbose_name = 'Прогресс'
        verbose_name_plural = 'Прогресс'
        unique_together = [('user','card')]
