from django.db import models
from cards.models import CardModel
from django.contrib.auth.models import User

class ProgressModel(models.Model):
    progress_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, models.CASCADE)
    card_id = models.ForeignKey(CardModel, models.CASCADE)
    attempts = models.IntegerField()
    successful_attempts = models.IntegerField()
