# Generated by Django 3.2 on 2021-05-08 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0020_auto_20210507_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Phone_Number',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
