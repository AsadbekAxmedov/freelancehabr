# Generated by Django 4.2.4 on 2023-12-22 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0003_order_price_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
