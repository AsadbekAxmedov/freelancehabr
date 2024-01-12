# Generated by Django 4.2.4 on 2023-12-22 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0002_response_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price_type',
            field=models.CharField(choices=[('HOUR', 'за час'), ('PROJECT', 'за проект'), ('NEGOTIABLE', 'договорная')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]