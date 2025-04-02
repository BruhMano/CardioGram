from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from api.views import CardViewset, DeckViewset, UserProgressViewset, UserViewset

router = routers.SimpleRouter()
router.register(r'card', CardViewset)
router.register(r'deck', DeckViewset)
router.register('progress', UserProgressViewset, 'progress')
router.register('user', UserViewset, 'user')

urlpatterns = [
    path('', include(router.urls)),
    path("auth/", views.obtain_auth_token),
]