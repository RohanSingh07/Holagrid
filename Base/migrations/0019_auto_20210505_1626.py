# Generated by Django 3.2 on 2021-05-05 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0018_auto_20210504_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stories',
            name='Time',
        ),
        migrations.AlterField(
            model_name='stories',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
