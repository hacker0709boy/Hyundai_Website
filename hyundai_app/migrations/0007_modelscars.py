# Generated by Django 3.2.15 on 2022-09-30 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hyundai_app', '0006_auto_20221001_0220'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelsCars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Model_Name', models.CharField(max_length=200)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='img')),
                ('Fuel', models.CharField(max_length=20)),
                ('Engine', models.CharField(max_length=20)),
                ('AWD_RWD', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]