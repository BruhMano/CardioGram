from django.shortcuts import render
from api.serializers import CardSerializer, DeckSerializer, UserProgressSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from cards.models import Card
from decks.models import Deck
from users_progress.models import Progress
from django.contrib.auth import get_user_model
from api.permissions import IsAdminOrReadOnly, IsAdminOrIsOwnerReadOnly

class CardViewset(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (IsAdminOrReadOnly, permissions.IsAuthenticated)

class DeckViewset(ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = (IsAdminOrReadOnly,)

class UserProgressViewset(ModelViewSet):
    serializer_class = UserProgressSerializer
    permission_classes = (IsAdminOrIsOwnerReadOnly,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Progress.objects.all()
        return Progress.objects.filter(user = self.request.user)

class UserViewset(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrIsOwnerReadOnly,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return get_user_model().objects.all()
        return get_user_model().objects.filter(id = self.request.user.id)