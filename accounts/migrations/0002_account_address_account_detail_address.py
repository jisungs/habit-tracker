# Generated by Django 4.2.1 on 2023-05-19 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='account',
            name='detail_address',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
