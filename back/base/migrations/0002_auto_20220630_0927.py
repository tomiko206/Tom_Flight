# Generated by Django 3.2.8 on 2022-06-30 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adminstrators',
            fields=[
                ('Id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('First_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Last_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Airline_Compamies',
            fields=[
                ('Id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('Id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('Id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('First_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Last_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Address', models.CharField(blank=True, max_length=50, null=True)),
                ('Phone_No', models.DecimalField(decimal_places=2, max_digits=50)),
                ('Credit_Card_No', models.DecimalField(decimal_places=2, max_digits=50)),
                ('User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('Id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Departure_Time', models.DateTimeField()),
                ('Landing_Time', models.DateTimeField()),
                ('Remaining_Tickets', models.CharField(blank=True, max_length=50, null=True)),
                ('Airline_Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.airline_compamies')),
                ('Destination_Country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destination_countrie', to='base.countries')),
                ('Origin_Country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin_countrie', to='base.countries')),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('Id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Customers', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.customers')),
                ('Flight', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.flights')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('Id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Username', models.TextField()),
                ('Password', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.CharField(blank=True, max_length=50, null=True)),
                ('User_Role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Users_Roles',
            fields=[
                ('Id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Role_Name', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='pita',
            name='user',
        ),
        migrations.DeleteModel(
            name='Note',
        ),
        migrations.DeleteModel(
            name='Pita',
        ),
        migrations.AddField(
            model_name='airline_compamies',
            name='Country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.countries'),
        ),
        migrations.AddField(
            model_name='airline_compamies',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]