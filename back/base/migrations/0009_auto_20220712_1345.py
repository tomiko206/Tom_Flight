# Generated by Django 3.2.8 on 2022-07-12 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0008_rename_user_customers_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminstrators',
            old_name='User',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='User',
            new_name='user',
        ),
        migrations.CreateModel(
            name='Airline_Companies',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.countries')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='flights',
            name='Airline_Company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.airline_companies'),
        ),
        migrations.DeleteModel(
            name='Airline_Compamies',
        ),
    ]