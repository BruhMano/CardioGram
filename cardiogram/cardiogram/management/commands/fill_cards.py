from cards.models import Card
from decks.models import Deck
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Заполняет базу данных тестовыми карточками'

    def handle(self, *args, **options):
        eng_file = open('data/nature_eng.txt', 'r')
        ru_file = open('data/nature_ru.txt', 'r', encoding='utf-8')
        for word in eng_file:
            word = word.strip()
            data = ru_file.readline().rstrip().split(' - ')
            card = Card(deck = Deck.objects.get(name = 'Nature'),front_text = word,
                        back_text = data[0], example_usage = data[1])
            card.save()