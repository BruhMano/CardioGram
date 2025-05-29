from rest_framework.serializers import ModelSerializer, Serializer, CharField, ValidationError
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
        fields = ['id', 'name', 'description', 'cover']

class UserProgressSerializer(ModelSerializer):
    class Meta:
        model = Progress
        fields = ['id', 'user', 'card','attempts', 'successful_attempts']

class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']

class ChangePasswordSerializer(Serializer):
    old_password = CharField(required=True)
    new_password = CharField(required=True)

    def validate_old_password(self, value):
        user = self.context['user']
        if not user.check_password(value):
            raise ValidationError("Current password is incorrect.")
        return value

    def validate(self, data):
        old_password = data.get('old_password')
        new_password = data.get('new_password')

        if old_password == new_password:
            raise ValidationError("New password must be different from the old password.")
        return data