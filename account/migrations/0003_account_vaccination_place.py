# Generated by Django 3.2 on 2021-04-28 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_vaccination_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='vaccination_place',
            field=models.CharField(blank=True, default=None, max_length=25, null=True),
        ),
    ]