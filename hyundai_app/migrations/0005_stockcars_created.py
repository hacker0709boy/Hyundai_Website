# Generated by Django 3.2.15 on 2022-09-30 21:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hyundai_app', '0004_stockcars'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockcars',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]