# Generated by Django 5.1.6 on 2025-03-28 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_card_deck_delete_cardmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='front_text',
            field=models.CharField(max_length=30),
        ),
    ]
