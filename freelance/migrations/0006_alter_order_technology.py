# Generated by Django 4.2.4 on 2023-12-22 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0005_remove_order_response_response_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='technology',
            field=models.ManyToManyField(related_name='order_technology', to='freelance.technology'),
        ),
    ]
