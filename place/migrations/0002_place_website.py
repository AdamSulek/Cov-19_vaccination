# Generated by Django 3.2 on 2021-05-01 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='website',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
