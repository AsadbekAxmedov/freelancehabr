# Generated by Django 4.2.4 on 2023-12-22 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0004_alter_order_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='response',
        ),
        migrations.AddField(
            model_name='response',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='freelance.order'),
            preserve_default=False,
        ),
    ]