# Generated by Django 3.2.8 on 2022-07-12 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20220712_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Avatar',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='CreatedTime',
        ),
    ]