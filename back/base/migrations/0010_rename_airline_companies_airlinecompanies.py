# Generated by Django 3.2.8 on 2022-07-12 14:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0009_auto_20220712_1345'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Airline_Companies',
            new_name='AirlineCompanies',
        ),
    ]
