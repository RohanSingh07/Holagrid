from django.db import models
from django.conf import settings
# Create your models here.
# HashTag
from django.contrib.auth.models import User
Gender = (
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others'),
)

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    UniqueCode = models.CharField(max_length=15,blank=True,null=True,unique=True)
    username = models.CharField(blank=True,null=True,max_length=50,unique=True)
    Profile_Name = models.CharField(max_length=100,blank=True,null=True)
    Profile_Photo = models.ImageField(blank=True,null=True,upload_to='Profile_Pictures')
    Bio = models.TextField(blank=True,null=True)
    Email = models.EmailField(blank=True,null=True,unique=True)
    Phone_Number = models.BigIntegerField(blank=True,null=True)
    Gender = models.CharField(max_length=20,blank=True,null=True,choices=Gender)
    Posts = models.ManyToManyField("Posts",blank=True)
    Stories = models.ManyToManyField("Stories",blank=True)
    Followers = models.ManyToManyField("self",blank=True,related_name='Follower',symmetrical=False)
    Following = models.ManyToManyField("self",blank=True,symmetrical=False)
    Chatrooms = models.ManyToManyField("Chatroom",blank=True)

class Stories(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    File = models.FileField(upload_to='Stories', blank=True, null=True)
    FileType = models.BooleanField(default=False, blank=True, null=True)
    Filter = models.CharField(blank=True, null=True, max_length=30)
    Text = models.TextField(blank=True,null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    Date = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Posts(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)

    File1 = models.FileField(upload_to='Posts', blank=True, null=True)
    File1Type = models.BooleanField(default=False,blank=True,null=True)

    File2 = models.FileField(upload_to='Posts', blank=True, null=True)
    File2Type = models.BooleanField(default=False, blank=True, null=True)

    File3 = models.FileField(upload_to='Posts', blank=True, null=True)
    File3Type = models.BooleanField(default=False, blank=True, null=True)

    File4 = models.FileField(upload_to='Posts', blank=True, null=True)
    File4Type = models.BooleanField(default=False, blank=True, null=True)

    File5 = models.FileField(upload_to='Posts', blank=True, null=True)
    File5Type = models.BooleanField(default=False, blank=True, null=True)

    File6 = models.FileField(upload_to='Posts', blank=True, null=True)
    File6Type = models.BooleanField(default=False, blank=True, null=True)

    File7 = models.FileField(upload_to='Posts', blank=True, null=True)
    File7Type = models.BooleanField(default=False, blank=True, null=True)

    File8 = models.FileField(upload_to='Posts', blank=True, null=True)
    File8Type = models.BooleanField(default=False, blank=True, null=True)

    File9 = models.FileField(upload_to='Posts', blank=True, null=True)
    File9Type = models.BooleanField(default=False, blank=True, null=True)

    File10 = models.FileField(upload_to='Posts', blank=True, null=True)
    File10Type = models.BooleanField(default=False, blank=True, null=True)

    Description = models.TextField(blank=True,null=True)
    Filter = models.CharField(blank=True,null=True,max_length=30)
    Comments = models.ManyToManyField("Comments",blank=True)
    Likes = models.ManyToManyField(Profile,blank=True,related_name="Post_Likes")
    Liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True)
    slug = models.SlugField(unique=True,blank=True,null=True)
    Date = models.DateField(auto_now_add=True,blank=True,null=True)
    Time = models.TimeField(auto_now_add=True,blank=True,null=True)



class Comments(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)
    Comment = models.TextField()
    Date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    Likes = models.ManyToManyField(Profile,blank=True,related_name="Likes")

# Model for storing chat
class Messages(models.Model):
    Channel_id = models.ForeignKey("Chatroom",on_delete=models.CASCADE)
    sender = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)
    message = models.TextField(blank=True,null=True)
    Timestamp = models.DateTimeField(auto_now_add=True)

# For storing messages
class Chatroom(models.Model):
    unique_id = models.CharField(unique=True,max_length=30)
    Messages = models.ManyToManyField(Messages,blank=True)
    Messengers = models.ManyToManyField(Profile,blank=True)











