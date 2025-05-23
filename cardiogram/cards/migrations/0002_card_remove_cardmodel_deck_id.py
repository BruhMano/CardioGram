# Generated by Django 5.1.6 on 2025-03-28 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front_text', models.CharField(max_length=30, unique=True)),
                ('back_text', models.CharField(max_length=30)),
                ('example_usage', models.TextField(null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Карта',
                'verbose_name_plural': 'Карты',
            },
        ),
        migrations.RemoveField(
            model_name='cardmodel',
            name='deck_id',
        ),
    ]
