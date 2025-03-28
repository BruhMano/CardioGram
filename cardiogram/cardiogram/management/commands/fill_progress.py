from cards.models import Card
from users_progress.models import Progress
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Заполняет базу данных тестовыми данными о прогрессе пользователя'

    def handle(self, *args, **options):
        data_file = open('data/progress.txt', 'r')
        for line in data_file:
            data = line.strip().split(' ')
            card = Card.objects.filter(front_text=data[1]).first()
            print(card)
            progress = Progress(user = get_user_model().objects.get(username = data[0]),
                                card = card,
                                attempts = data[3],successful_attempts = data[2])
            progress.save()