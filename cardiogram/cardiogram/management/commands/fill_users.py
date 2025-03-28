from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Заполняет базу данных тестовыми пользователями'

    def handle(self, *args, **options):
        data_file = open('data/users.txt', 'r', encoding = 'utf-8')
        user_model = get_user_model()
        for line in data_file:
            data = line.strip().split(' ')
            user = user_model(username = data[0], first_name = data[1],
                              last_name = data[2], email = data[3])
            user.set_password(data[4])
            user.save()