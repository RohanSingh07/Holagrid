# Generated by Django 3.2 on 2021-04-30 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0015_auto_20210429_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='UniqueCode',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
