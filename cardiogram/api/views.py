from django.shortcuts import render
from api.serializers import CardSerializer, DeckSerializer, UserProgressSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from cards.models import Card
from decks.models import Deck
from users_progress.models import Progress
from django.contrib.auth import get_user_model
from api.permissions import IsAdminOrReadOnly, IsOwner

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
    permission_classes = (IsAdminOrReadOnly, IsOwner)

    def get_queryset(self):
        return Progress.objects.filter(user = self.request.user)

class UserViewset(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly, IsOwner)

    def get_queryset(self):
        return Card.objects.filter(user = self.request.user)