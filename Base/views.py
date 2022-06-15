from django.contrib import messages
from . import models
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect,reverse
from django.contrib.auth.models import auth
from datetime import datetime,timedelta,date
from django.http import JsonResponse,HttpResponse
import json
from django.core import serializers
from users.models import Account
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import moviepy.editor
import os
from core.settings import BASE_DIR
from datetime import timezone


@login_required
def HomeView(request):
    Profile = models.Profile.objects.get(user =request.user)
    # I can only see the profile and posts of following persons
    Posts = []
    Stories =[]
    Followings = Profile.Following.all()
    Followers = Profile.Following.all()
    # Get all the stories of last 24 hrs
    #time_threshold = datetime.now() - timedelta(hours=24)
    # status = Profile.Stories.filter(Date__gte=time_threshold)
    status = Profile.Stories.all()
    # MyPosts = Profile.Posts.filter(Date=datetime.now().date())
    MyPosts = Profile.Posts.all()
    Posts.append(MyPosts)
    for Following in Followings:
        # Only New Posts can be seen todays and yesterdays
        # PostsToday = Following.Posts.filter(Date=datetime.now().date())
        PostsToday = Following.Posts.all()
        Posts.append(PostsToday)
        # PostsYes = Following.Posts.filter(Date = (datetime.now()-timedelta(1)).date())
        # PostsYes = Following.Posts.all()
        # Posts.append(PostsYes)
        # Get all the stories of other users
        # Story = Following.Stories.filter(Date__gte=time_threshold)
        Story = Following.Stories.all()
        if Story:
            Stories.append(Following)
    if Followings:
        New = 0
    else:
        New = 1
    return render(request,'index.html',{
        'AllPosts':Posts,
        'Profile':Profile,
        'Status':status,
        'OtherStories':Stories,
        'Followers':Followers,
        'Followings':Followings,
        'New':New

    })

def CommentView(request,postslug):
    post = models.Posts.objects.get(slug=postslug)
    Profile = models.Profile.objects.get(user =request.user)
    return render(request,'comments.html',{
        'post':post,
        'profile':Profile
    })


def LikesView(request,postslug):
    post = models.Posts.objects.get(slug=postslug)
    return render(request, 'Likes.html', {
        'post': post
    })

@login_required
def ProfileView(request,slug):
    Profile = models.Profile.objects.get(user__username=slug)
    MyProfile = models.Profile.objects.get(user=request.user)
    # To Check if the user is the owner of profile or not
    if Profile.user == MyProfile.user:
        Admin = True
    else:
        Admin = False
    # your Followers and Following
    return render(request,'ProfilePage.html',
                  {
                   'Profile':Profile,
                   'MyProfile':MyProfile,
                   'Admin':Admin,

                   })


# For adding new posts
@login_required
def AddPost(request):
    if request.method =='GET':
        return render(request,'AddPost.html',{})
    else:
        Profile = models.Profile.objects.get(user = request.user)
        File = request.FILES.getlist('File[]')
        Filter = request.POST['FilterInput']
        Caption = request.POST['Caption']
        new_post = models.Posts(
            user = Profile,
            Filter = Filter,
            Description = Caption,

        )
        File1 = File[0]
        File1Type = request.POST['File1type'] == 'Video'
        new_post.File1 = File1
        new_post.File1Type = File1Type

        if len(File)>1:
            File2 = File[1]
            File2Type = request.POST['File2type'] == 'Video'
            new_post.File2 = File2
            new_post.File2Type = File2Type
        if len(File) > 2:
            File3 = File[2]
            File3Type = request.POST['File3type'] == 'Video'
            new_post.File3 = File3
            new_post.File3Type = File3Type

        if len(File) > 3:
            File4 = File[3]
            File4Type = request.POST['File4type'] == 'Video'
            new_post.File4 = File4
            new_post.File4Type = File4Type
        if len(File) > 4:
            File5 = File[4]
            File5Type = request.POST['File5type'] == 'Video'
            new_post.File5 = File5
            new_post.File5Type = File5Type
        if len(File) > 5:
            File6 = File[5]
            File6Type = request.POST['File6type'] == 'Video'
            new_post.File6 = File6
            new_post.File6Type = File6Type
        if len(File) > 6:
            File7 = File[6]
            File7Type = request.POST['File7type'] == 'Video'
            new_post.File7 = File7
            new_post.File7Type = File7Type
        if len(File) > 7:
            File8 = File[7]
            File8Type = request.POST['File8type'] == 'Video'
            new_post.File8 = File8
            new_post.File8Type = File8Type
        if len(File) > 8:
            File9 = File[8]
            File9Type = request.POST['File9type'] == 'Video'
            new_post.File9 = File9
            new_post.File9Type = File9Type
        if len(File) > 9:
            File10 = File[9]
            File10Type = request.POST['File10type'] == 'Video'
            new_post.File10 = File10
            new_post.File10Type = File10Type

        new_post.slug = Profile.user.username+'-Posts-'+datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
        new_post.save()
        Profile.Posts.add(new_post)
        messages.info(request, 'Posted Successfully')
        return redirect('Base:HomeView')

# View for Explore
def ExploreView(request):
    Posts = models.Posts.objects.all()
    posts = serializers.serialize('json',Posts)
    Profile = models.Profile.objects.get(user = request.user)
    return render(request,'Explore.html',{
        'Posts':json.dumps(posts),
        'p':Posts,
        'Postcount':len(Posts),
        'Profile':Profile
    })


# For Searching New users
def Search(request,SearchInput):

    Result = models.Profile.objects.filter(user__username= SearchInput)

    data = serializers.serialize('json',Result)

    return JsonResponse(data,safe=False)

# For Editing Profile
@login_required
def ProfileEdit(request,slug):
    Profile = models.Profile.objects.get(user__username=request.user)
    User = Account.objects.get(username = request.user)
    if request.method == 'GET':
        return render(request,'ProfileEdit.html',{
            'Profile':Profile,
        })
    else:
        # If there is change in the photo
        if request.FILES.get('ProfilePhoto'):
            ProfilePhoto = request.FILES['ProfilePhoto']
            Profile.Profile_Photo = ProfilePhoto
        Profile.Profile_Name = request.POST['Profile_Name']
        Profile.username = request.POST['Username_Name']
        User.username = request.POST['Username_Name']
        Profile.Bio = request.POST['BioVal']
        Profile.save()
        User.save()
        return redirect('Base:ProfileEdit',slug=slug)


# All Chats Page
def AllChats(request):
    MyProfile = models.Profile.objects.get(user = request.user)
    return render(request,'AllChats.html',{
        'Profile':MyProfile
    })

from users.models import Account
def Chatroom(request,user1,user2):
    Sender1 = models.Profile.objects.get(UniqueCode = user1)
    Sender2 = models.Profile.objects.get(UniqueCode = user2)
    # Check if the Chatroom with these two already exists
    Unilist = [int(Sender1.UniqueCode),int(Sender2.UniqueCode)]
    Unilist.sort()
    id = str(Unilist[0])+str(Unilist[1])
    Chatroom = Sender1.Chatrooms.filter(unique_id =id)
    if Chatroom.exists():
        Chatroom = Chatroom[0]
    else:
        New_Chatroom = models.Chatroom(
            unique_id =id
        )
        New_Chatroom.save()
        Sender1.Chatrooms.add(New_Chatroom)
        Sender2.Chatrooms.add(New_Chatroom)
        New_Chatroom.Messengers.add(Sender1)
        New_Chatroom.Messengers.add(Sender2)
        Chatroom = New_Chatroom
    return render(request,'Chatroom.html',{
        'Chatroom':Chatroom,
        'Sender1':Sender1,
        'Sender2':Sender2,

    })

# Function to Send Reply from Status
def SendReply(request):
    Sender1 = models.Profile.objects.get(user__username = request.GET.get('user1')) # Sender of the Message
    Sender2 = models.Profile.objects.get(user__username = request.GET.get('user2'))
    # Check if the Chatroom with these two already exists
    Unilist = [int(Sender1.UniqueCode),int(Sender2.UniqueCode)]
    Unilist.sort()
    id = str(Unilist[0])+str(Unilist[1])
    Chatroom = Sender1.Chatrooms.filter(unique_id =id)
    if Chatroom.exists():
        Chatroom = Chatroom[0]
    else:
        New_Chatroom = models.Chatroom(
            unique_id =id
        )
        New_Chatroom.save()
        Sender1.Chatrooms.add(New_Chatroom)
        Sender2.Chatrooms.add(New_Chatroom)
        New_Chatroom.Messengers.add(Sender1)
        New_Chatroom.Messengers.add(Sender2)
        Chatroom = New_Chatroom
    # Save the Message to the Chatroom
    New_message = models.Messages(
        Channel_id = Chatroom,
        sender = Sender1,
        message = request.GET.get('message')
    )
    New_message.save()
    Chatroom.Messages.add(New_message)
    return HttpResponse(New_message)

# function to save the messages to DB
def SaveMessage(request):
    if request.method == 'GET':
        user = request.GET.get('user')
        Msg = request.GET.get('Msg')
        Chatroom_id = request.GET.get('Chatroom_id')
        sender = models.Profile.objects.get(user__username = user)
        chatroom = models.Chatroom.objects.get(unique_id=Chatroom_id)
        Message = models.Messages(
            Channel_id=chatroom,
            sender = sender,
            message = Msg
        )
        Message.save()
        chatroom.Messages.add(Message)
        return HttpResponse(Msg)

# View for saving comment
def SaveComment(request):
    post_name = request.GET.get('post')
    user = request.GET.get('user')
    comment = request.GET.get('Comment')
    post = models.Posts.objects.get(slug=post_name)
    profile = models.Profile.objects.get(user__username=user)
    comment = models.Comments(
       user = profile,
       Comment = comment,
    )
    comment.save()
    post.Comments.add(comment)
    post.save()
    return HttpResponse(comment)


# For ExplorePosts
def ExplorePosts(request,slug):
    Profile = models.Profile.objects.get(user__username = request.user.username)
    Posts = models.Posts.objects.filter(slug=slug)
    return render(request,'ExplorePost.html',{
        'Profile':Profile,
        'AllPosts':[Posts]
    })


# For Uploading status
def StatusView(request):
    Profile = models.Profile.objects.get(user__username=request.user.username)
    if request.method =='GET':
        # Get all the stories of last 24 hrs
        time_threshold = datetime.now() -timedelta(hours=24)
        status= Profile.Stories.filter(Date__gte=time_threshold)
        return render(request,'status.html',{
            'Profile': Profile,
            'Status':status
        })
    else:
        Input = request.FILES.getlist('StoryInput[]')
        Filetype = request.POST.get('Filetype')
        if Filetype =='Video':
            Save_video = models.Stories(
                user=Profile,
                File=Input[0],
                FileType=Filetype == 'Video',
                slug=Profile.user.username + '-Story-' + datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            )
            Save_video.save()
            Profile.Stories.add(Save_video)
            video = moviepy.editor.VideoFileClip(os.path.join(BASE_DIR,'media/'+str(Save_video.File)))
            # Contains the duration of the video in terms of seconds
            video_duration = int(video.duration)
            #Temporary store the File
            # If the file duration is greater than 60 seconds trim it
            if video_duration>60:
                f = open(os.path.join(BASE_DIR,'media/'+str(Save_video.File)[:8]+'Short'+str(Save_video.File)[8:]), "w")
                ffmpeg_extract_subclip( os.path.join(BASE_DIR,'media/'+str(Save_video.File)),0, 60, targetname=os.path.join(BASE_DIR,'media/'+str(Save_video.File)[:8]+'Short'+str(Save_video.File)[8:]))
                Save_video.delete()
                Save_video = models.Stories(
                    user=Profile,
                    File=os.path.join(BASE_DIR,'media/'+str(Save_video.File)[:8]+'Short'+str(Save_video.File)[8:]),
                    FileType=Filetype == 'Video',
                    slug = Profile.user.username+'-Story-'+datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                )
                Save_video.save()
                Profile.Stories.add(Save_video)
        else:
            Save_video = models.Stories(
                user=Profile,
                File=Input[0],
                FileType = Filetype =='Video',
                slug=Profile.user.username+'-Story-'+datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            )
            Save_video.save()
            Profile.Stories.add(Save_video)
        return redirect('Base:HomeView')

# For Watching Status
@login_required
def Statuses(request,user):
    Profile = models.Profile.objects.get(user__username=user)
    # Get all the stories of last 24 hrs
    time_threshold = datetime.now() - timedelta(hours=30)
    # status = Profile.Stories.filter(Date__gte=time_threshold)
    status = Profile.Stories.all()
    return render(request,'StatusShow.html',{
        'Profile': Profile,
        'Status': status,

    })

def AddRemFollower(request):
    MyProfile = request.GET.get('MyProfile')
    Profile = request.GET.get('Profile')
    Request = request.GET.get('Request')
    Myprofile = models.Profile.objects.get(user__username = MyProfile)
    profile = models.Profile.objects.get(user__username = Profile)
    if Request == 'Follow':
        profile.Followers.add(Myprofile)
        Myprofile.Following.add(profile)
    else:
        profile.Followers.remove(Myprofile)
        Myprofile.Following.remove(profile)

    return JsonResponse('Hello',safe=False)    

# Rest API
from rest_framework import viewsets

from .serializers import PostSerializer
from users.models import Account
# Creating a Viewset which will return JSON data of our model POST
class PostViewSet(viewsets.ModelViewSet):
    """
    Returns Json list of all Posts
    """
    queryset = models.Posts.objects.all()
    serializer_class = PostSerializer

# Viewset for accounts
class AccountViewSet(viewsets.ModelViewSet):
    """
    Returns Json list of all Posts
    """
    queryset = Account.objects.all()
    serializer_class = PostSerializer

# for user login
def AppLogin(request,username,password):
    # Check of the user exists
    user = Account.objects.filter(username=username)
    if user.exists():
        # Check if the password is right
        userauth = auth.authenticate(username=username, password=password)
        if userauth is not None:
            Profile = [models.Profile.objects.get(user=user[0])]
            result =serializers.serialize('json',Profile)
        else:
            result=False    
    else:
        result=False    
    return JsonResponse(result,safe=False)