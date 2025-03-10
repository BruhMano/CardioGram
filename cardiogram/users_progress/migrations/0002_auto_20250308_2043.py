# Generated by Django 5.1.6 on 2025-03-08 16:43

from django.db import migrations
from django.contrib.auth import get_user_model
from os.path import dirname

def add_users(apps, shema_editor):
    user_model = get_user_model()
    users = open(dirname(__file__)+'/users.txt', 'r', encoding='utf-8')
    for user in users:
        data = user.split(' ')
        user_model.objects.create(username = data[0], first_name = data[1], last_name = data[2], email = data[3],
                                  password = data[4])

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users_progress', '0001_initial')
    ]

    operations = [
        migrations.RunPython(add_users)
    ]
