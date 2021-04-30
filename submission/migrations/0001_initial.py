# Generated by Django 3.2 on 2021-04-28 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dialisis', models.BooleanField(default=False)),
                ('cancers', models.BooleanField(default=False)),
                ('transplant', models.BooleanField(default=False)),
                ('thrombosis', models.BooleanField(default=False)),
                ('chronic', models.BooleanField(default=False)),
                ('drugs', models.CharField(blank=True, max_length=100, null=True)),
                ('additional_question', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
    ]