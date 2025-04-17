from django.urls import path, include
from rest_framework import routers
from api.views import DeckViewset, UserProgressViewset, UserViewset

router = routers.SimpleRouter()
# router.register(r'card', CardViewset)
router.register(r'deck', DeckViewset)
router.register(r'progress', UserProgressViewset, 'progress')
router.register(r'user', UserViewset, 'user')

urlpatterns = [
    path('', include(router.urls)),
]