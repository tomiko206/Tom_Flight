# Generated by Django 3.2.8 on 2022-08-24 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_ticket_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='Customer',
        ),
    ]
