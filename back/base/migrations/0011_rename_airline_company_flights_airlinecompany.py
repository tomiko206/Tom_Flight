# Generated by Django 3.2.8 on 2022-07-12 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_rename_airline_companies_airlinecompanies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flights',
            old_name='Airline_Company',
            new_name='AirlineCompany',
        ),
    ]
