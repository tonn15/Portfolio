# Generated by Django 5.1.2 on 2024-10-18 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('ingredients', models.CharField(max_length=400)),
                ('prix', models.FloatField(default=0)),
                ('vegetarienne', models.BooleanField(default=False)),
            ],
        ),
    ]
