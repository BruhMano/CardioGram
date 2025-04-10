# Generated by Django 5.1.6 on 2025-03-06 15:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('decks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardModel',
            fields=[
                ('card_id', models.IntegerField(primary_key=True, serialize=False)),
                ('front_text', models.CharField(max_length=30)),
                ('back_text', models.CharField(max_length=30)),
                ('example_usage', models.TextField()),
                ('deck_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decks.deckmodel')),
            ],
        ),
    ]
