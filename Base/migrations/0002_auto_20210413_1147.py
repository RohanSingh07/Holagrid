# Generated by Django 3.2 on 2021-04-13 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='Comments',
            field=models.ManyToManyField(blank=True, to='Base.Comments'),
        ),
    ]
