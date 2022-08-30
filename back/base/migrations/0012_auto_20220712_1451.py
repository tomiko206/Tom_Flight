# Generated by Django 3.2.8 on 2022-07-12 14:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0011_rename_airline_company_flights_airlinecompany'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AirlineCompanies',
            new_name='Airline_Companies',
        ),
        migrations.RenameField(
            model_name='flights',
            old_name='AirlineCompany',
            new_name='Airline_Company',
        ),
    ]