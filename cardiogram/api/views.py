from api.serializers import CardSerializer, DeckSerializer, UserProgressSerializer, UserSerializer, ChangePasswordSerializer
from rest_framework.response import Response
from rest_framework import permissions, generics, views
from cards.models import Card
from decks.models import Deck
from users_progress.models import Progress
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class CardRetrieve(generics.RetrieveAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]

class DeckList(generics.ListAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

class DeckRetrieve(generics.RetrieveAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        deck = self.get_object()
        queryset = (Card.objects.filter(deck = deck)
                    .exclude(id__in = [card.id for card in
                                       Progress.objects.filter(user = request.user)]))
        serializer = CardSerializer(queryset, many = True)
        return Response(serializer.data)

class UserProgressListCreate(generics.ListCreateAPIView):
    serializer_class = UserProgressSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Progress.objects.all()
        return Progress.objects.filter(user = self.request.user.id)

    def post(self, request, *args, **kwargs):
        progress_record = Progress.objects.create(
            user = request.user,
            card = Card.objects.get(id = request.data.get('card')),
            attempts = 0,
            successful_attempts = 0
        )
        progress_record.save()
        return Response("Card added to your deck successfully!",200)

class UserAnswerCheck(generics.UpdateAPIView):
    serializer_class = UserProgressSerializer
    def patch(self, request, action, *args, **kwargs):
        if action == "right":
            progress = Progress.objects.get(card = request.data.get('card_id'), user = request.user)
            progress.attempts += 1
            progress.successful_attempts += 1
            serializer = self.get_serializer(progress, data=request.data, partial= True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        elif action == "wrong":
            progress = Progress.objects.get(card = request.data.get('card_id'), user = request.user)
            progress.attempts += 1
            serializer = self.get_serializer(progress, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)

class UserList(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return get_user_model().objects.filter(id = self.request.user.id)

class UserDelete(views.APIView):
    def delete(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return Response("Not allowed to do this. You need to login first.", 401)
        user.delete()
        response = Response({'message': 'Account deleted successfully!'}, 200)
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')

        return response

class UserAuth(views.APIView):
    def post(self, request, action, *args, **kwargs):
        if action == "change-password":
            if not request.user.is_authenticated:
                return Response("Not allowed to do this. You need to login first.", 401)
            user = request.user
            serializer = ChangePasswordSerializer(data=request.data, context={'user': user})

            if serializer.is_valid():
                new_password = serializer.validated_data['new_password']
                user.set_password(new_password)
                user.save()

                return Response({"message": "Password changed successfully."}, status=200)

            return Response(serializer.errors, status=400)
        elif action == "logout":
            if not request.user.is_authenticated:
                return Response("Not allowed to do this. You need to login first.", 401)
            refresh_token = request.COOKIES.get('refresh_token')
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()

            response = Response({'message': 'Logout successful'})
            response.delete_cookie('refresh_token')
            response.delete_cookie('access_token')
            return response
        elif action == "login":
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(username=username, password=password)
            if user is None:
                return Response({'error': 'Invalid credentials. Try again!'}, status=401)

            refresh = RefreshToken.for_user(user)
            response = Response()
            response.set_cookie(
                key='refresh_token',
                value=str(refresh),
                secure=False,
                httponly=True,
                samesite='Lax'
            )
            response.set_cookie(
                key='access_token',
                value=str(refresh.access_token),
                secure=False,
                httponly=True,
                samesite='Lax'
            )
            response.data = {
                'message': 'Login successful'
            }
            return response
        elif action == "register":
            if get_user_model().objects.filter(username = request.data.get('username')).exists():
                return Response("User already exists!", 400)
            user = get_user_model().objects.create(
                username = request.data.get('username'),
                email = request.data.get('email'),
                first_name = request.data.get('first_name'),
                last_name = request.data.get('last_name')
            )
            user.set_password(request.data.get('password'))
            user.save()
            login_res = self.post(request, action='login')
            return login_res
        elif action == 'edit':
            if get_user_model().objects.filter(username = request.data.get('username')).exists():
                return Response("User already exists!", 400)
            user = request.user
            user.username=request.data.get('username')
            user.email=request.data.get('email')
            user.first_name=request.data.get('first_name')
            user.last_name=request.data.get('last_name')
            user.save()
            return Response("Profile editing complited successfully!",200)
        else:
            return Response(f"Bad Request. We dont have {action}/ page...", status = 400)