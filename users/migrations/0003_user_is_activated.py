# Generated by Django 5.0 on 2023-12-29 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_activated',
            field=models.BooleanField(default=False),
        ),
    ]
