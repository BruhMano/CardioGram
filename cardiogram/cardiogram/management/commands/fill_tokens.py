from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    def handle(self, *args, **options):

        for user in get_user_model().objects.all():
            Token.objects.get_or_create(user=user)