from django.db import models
from cards.models import Card
from django.contrib.auth.models import User

class Progress(models.Model):
    progress_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, models.CASCADE)
    card_id = models.ForeignKey(Card, models.CASCADE)
    attempts = models.IntegerField()
    successful_attempts = models.IntegerField()
