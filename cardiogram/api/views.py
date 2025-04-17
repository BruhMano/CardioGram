from debugpy.adapter import access_token
from django.shortcuts import render
from api.serializers import CardSerializer, DeckSerializer, UserProgressSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.decorators import action, permission_classes
from cards.models import Card
from decks.models import Deck
from users_progress.models import Progress
from django.contrib.auth import get_user_model
from api.permissions import IsAdminOrReadOnly, IsAdminOrIsOwnerReadOnly
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

# class CardViewset(ModelViewSet):
#     queryset = Card.objects.all()
#     serializer_class = CardSerializer
#     permission_classes = (IsAdminOrReadOnly, permissions.IsAuthenticated)

class DeckViewset(ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def retrieve(self, request, *args, **kwargs):
        deck = self.get_object()
        queryset = (Card.objects.filter(deck = deck)
                    .exclude(id__in = [card.id for card in
                                       Progress.objects.filter(user = request.user)]))
        serializer = CardSerializer(queryset, many = True)
        return Response(serializer.data)

class UserProgressViewset(ModelViewSet):
    serializer_class = UserProgressSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Progress.objects.all()
        return Progress.objects.filter(user = self.request.user.id)

    def list(self, request, *args, **kwargs):
        progresses = self.get_queryset()
        queryset = [progress.card for progress in progresses]
        serializer = CardSerializer(queryset, many = True)
        return Response(serializer.data)


    @action(detail=False, methods=["PATCH"])
    def right(self, request, pk = None):
        progress = Progress.objects.get(card = request.data.get('card_id'))
        progress.attempts += 1
        progress.successful_attempts += 1
        serializer = self.get_serializer(progress, data=request.data, partial= True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=False, methods=["PATCH"])
    def wrong(self, request, pk = None):
        progress = Progress.objects.get(card = request.data.get('card_id'))
        progress.attempts += 1
        serializer = self.get_serializer(progress, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class UserViewset(ModelViewSet):
    serializer_class = UserSerializer
    # permission_classes = (IsAdminOrIsOwnerReadOnly, permissions.IsAuthenticated)

    def get_queryset(self):
        if self.request.user.is_staff:
            return get_user_model().objects.all()
        return get_user_model().objects.filter(id = self.request.user.id)

    @action(detail = False, methods = ["PATCH"])
    def change_password(self):
        pass

    @action(detail = False, methods = ["POST"])
    def login(self, request):
        # permission_classes = (permissions.AllowAny,)

        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=401)

        refresh = RefreshToken.for_user(user)
        response = Response()
        response.set_cookie(
            key='refresh_token',
            value=str(refresh),
            httponly=True,
            samesite='Lax'
        )
        response.set_cookie(
            key='access_token',
            value=str(refresh.access_token),
            httponly=True,
            samesite='Lax'
        )
        response.data = {
            'message': 'Login successful'
        }
        return response

    @action(detail = False, methods = ["POST"])
    def logout(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()

        response = Response({'message': 'Logout successful'})
        response.delete_cookie('refresh_token')
        response.delete_cookie('access_token')
        return response

    @action(detail=False, methods=["POST"])
    def register(self, request):
        user = get_user_model().objects.create(
            username = request.data.get('username'),
            email = request.data.get('email'),
            first_name = request.data.get('fname'),
            last_name = request.data.get('lname')
        )
        user.set_password(request.data.get('password'))
        user.save()
        return Response({
            'message': 'Registration successful'
        })
