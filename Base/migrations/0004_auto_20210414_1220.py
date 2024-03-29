# Generated by Django 3.2 on 2021-04-14 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Base', '0003_posts_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='Photo1',
        ),
        migrations.AddField(
            model_name='comments',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='File1',
            field=models.FileField(blank=True, null=True, upload_to='Posts'),
        ),
        migrations.AddField(
            model_name='posts',
            name='File10',
            field=models.FileField(blank=True, null=True, upload_to='Posts'),
        ),
        migrations.AddField(
            model_name='posts',
            name='File2',
            field=models.FileField(blank=True, null=True, upload_to='Posts'),
        ),
        migrations.AddField(
            model_name='posts',
            name='File3',
            field=models.FileField(blank=True, null=True, upload_to='Posts'),
        ),
        migrations.AddField(
            model_name='posts',
            name='File4',
            field=models.FileField(blank=True, null=True, upload_to='Posts'),
        ),
        migrations.AddField(
            model_name='posts',
            name='File5',
            field=models.FileField(blank=True, null=True, upload_to='Posts'),
        ),
        migrations.AddField(
            model_name='posts',
            name='File6',
            field=models.FileField(blank=True, null=True, upload_to='Posts'),
        ),
        migrations.AddField(
            model_name='posts',
            name='File7',
            field=models.FileField(blank=True, null=True, upload_to='Posts'),
        ),
        migrations.AddField(
            model_name='posts',
            name='File8',
            field=models.FileField(blank=True, null=True, upload_to='Posts'),
        ),
        migrations.AddField(
            model_name='posts',
            name='File9',
            field=models.FileField(blank=True, null=True, upload_to='Posts'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='Description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Profile_Photo', models.ImageField(blank=True, null=True, upload_to='Profile_Pictures')),
                ('Bio', models.TextField(blank=True, null=True)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('Phone_Number', models.IntegerField(blank=True, null=True)),
                ('Gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=20, null=True)),
                ('Followers', models.ManyToManyField(blank=True, related_name='_Base_profile_Followers_+', to='Base.Profile')),
                ('Following', models.ManyToManyField(blank=True, related_name='_Base_profile_Following_+', to='Base.Profile')),
                ('Posts', models.ManyToManyField(blank=True, to='Base.Posts')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='Likes',
            field=models.ManyToManyField(blank=True, related_name='Likes', to='Base.Profile'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Base.profile'),
        ),
        migrations.AddField(
            model_name='posts',
            name='Likes',
            field=models.ManyToManyField(blank=True, to='Base.Profile'),
        ),
    ]
