# Generated by Django 4.2.4 on 2024-01-08 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0007_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='freelance.order'),
        ),
    ]
