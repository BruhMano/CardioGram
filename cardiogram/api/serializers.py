from rest_framework.serializers import ModelSerializer
from cards.models import Card
from decks.models import Deck
from users_progress.models import Progress
from django.contrib.auth import get_user_model

class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'deck', 'front_text', 'back_text', 'example_usage']

class DeckSerializer(ModelSerializer):
    class Meta:
        model = Deck
        fields = ['id', 'name', 'description']

class UserProgressSerializer(ModelSerializer):
    class Meta:
        model = Progress
        fields = ['id', 'user', 'card','attempts', 'successful_attempts']

class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'is_staff']