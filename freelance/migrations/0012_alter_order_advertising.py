# Generated by Django 5.0.1 on 2024-01-11 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0011_order_advertising'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='advertising',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
