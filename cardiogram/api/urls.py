from django.urls import path
from api.views import UserProgressListCreate, UserAnswerCheck, CardRetrieve, DeckList
from api.views import DeckRetrieve, UserList, UserAuth, UserDelete

urlpatterns = [
    path('card/<int:pk>/', CardRetrieve.as_view()),
    path('deck/', DeckList.as_view()),
    path('deck/<int:pk>/', DeckRetrieve.as_view()),
    path('auth/<str:action>/', UserAuth.as_view()),
    path('profile/', UserList.as_view()),
    path('progress/', UserProgressListCreate.as_view()),
    path('progress/<str:action>/', UserAnswerCheck.as_view()),
    path('delete/', UserDelete.as_view()),
]