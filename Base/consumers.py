# This is like the views for Routing
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from . import models
from channels.db import database_sync_to_async
from users.models import Account
from django.core import serializers
from itertools import chain
class HomePage(AsyncWebsocketConsumer):

    async def connect(self):
        # Get the name of the chatroom
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Construct a new group
        await self.channel_layer.group_add(
            self.room_group_name,
            # Contains the pointer to the channel layer instance
            self.channel_name
        )

        # The application must accept the connection or reject it
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self ,text_data):
        # get the data
        text_data_json = json.loads(text_data)
        # extract it
        post_name = text_data_json['post_name']
        user = text_data_json['user']
        # Now send the data back to the group
        await self.channel_layer.group_send(
            self.room_group_name,{
                'type':'Home_Calls',
                'post_name':post_name,
                'user':user
            }
        )

    # We use this decorator to connect to database inside consumers
    @database_sync_to_async
    def AddRemLike(self,user,post_name):
        post = models.Posts.objects.get(slug=post_name)
        profile = models.Profile.objects.get(user__username = user)
        user_prof = Account.objects.get(username=user)
        if user_prof not in post.Liked_by.all():
            post.Likes.add(profile)
            post.Liked_by.add(user_prof)
            post.save()
        else:
            post.Likes.remove(profile)
            post.Liked_by.remove(user_prof)
            post.save()
        posts = models.Posts.objects.all()
        return posts

    async def Home_Calls(self, event):
        post_name = event['post_name']
        user = event['user']
        await self.AddRemLike(user,post_name)
        await self.send(text_data=json.dumps({
            'user':user,
            'post_name': post_name,

        }))

# For Comment Section
class CommentPage(AsyncWebsocketConsumer):
    async def connect(self):
        # Get the name of the chatroom
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Construct a new group
        await self.channel_layer.group_add(
            self.room_group_name,
            # Contains the pointer to the channel layer instance
            self.channel_name
        )

        # The application must accept the connection or reject it
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self ,text_data):
        # get the data
        text_data_json = json.loads(text_data)
        # extract it
        post_name = text_data_json['post_name']
        user = text_data_json['user']
        comment = text_data_json['comment']
        # Now send the data back to the group
        await self.channel_layer.group_send(
            self.room_group_name,{
                'type':'Comment_Calls',
                'post_name':post_name,
                'user':user,
                'comment':comment,
            }
        )

    # for adding comment
    @database_sync_to_async
    def AddRemComment(self, user):

        profile = models.Profile.objects.get(user__username=user)
        Profile = [profile]
        return serializers.serialize('json',Profile)

    async def Comment_Calls(self, event):
        post_name = event['post_name']
        user = event['user']
        comment = event['comment']
        profile = await self.AddRemComment(user)
        await self.send(text_data=json.dumps({
            'user':profile,
            'post_name': post_name,
            'comment':comment

        }))


# For explore
class ExplorePage(AsyncWebsocketConsumer):

    async def connect(self):
        # Get the name of the chatroom
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Construct a new group
        await self.channel_layer.group_add(
            self.room_group_name,
            # Contains the pointer to the channel layer instance
            self.channel_name
        )

        # The application must accept the connection or reject it
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self ,text_data):
        # get the data
        text_data_json = json.loads(text_data)
        # extract it
        SearchInput = text_data_json['SearchInput']
        # Now send the data back to the group
        await self.channel_layer.group_send(
            self.room_group_name,{
                'type':'ExploreSearch',
                'SearchInput':SearchInput,
            }
        )
    @database_sync_to_async
    def Search(self,SearchInput):
        searchres1 = models.Profile.objects.filter(user__username__contains=SearchInput )
        searchres2 = models.Profile.objects.filter(Profile_Name__contains=SearchInput)
        searchres_f = list(set(chain(searchres1,searchres2)))
        searchres = serializers.serialize('json', searchres_f)
        return searchres

    async def ExploreSearch(self, event):
        SearchInput = event['SearchInput']
        results = await self.Search(SearchInput)

        await self.send(text_data=json.dumps({
            'results': results
        }))

# For Profile Page

class ProfilePage(AsyncWebsocketConsumer):

    async def connect(self):
        # Get the name of the chatroom
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Construct a new group
        await self.channel_layer.group_add(
            self.room_group_name,
            # Contains the pointer to the channel layer instance
            self.channel_name
        )

        # The application must accept the connection or reject it
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self ,text_data):
        # get the data
        text_data_json = json.loads(text_data)
        # extract it
        MyProfile = text_data_json['MyProfile'] # The requestor
        Profile = text_data_json['Profile'] # The profile to which request is being made
        Request = text_data_json['Request']
        # Now send the data back to the group
        await self.channel_layer.group_send(
            self.room_group_name,{
                'type':'ProfilePageFunc',
                'MyProfile':MyProfile,
                'Profile':Profile,
                'Request':Request
            }
        )

    async def ProfilePageFunc(self,event):
        MyProfile = event['MyProfile']# The requestor
        Profile = event['Profile']  # The Profile where follower will be added
        Request = event['Request']
        await self.send(text_data=json.dumps({
            'MyProfile': MyProfile,
            'Profile': Profile,
        }))

# For Chatroom Between users
class Chatroom(AsyncWebsocketConsumer):
    async def connect(self):
        # Get the name of the chatroom
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Construct a new group
        await self.channel_layer.group_add(
            self.room_group_name,
            # Contains the pointer to the channel layer instance
            self.channel_name
        )
        # The application must accept the connection or reject it
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # get the data
        text_data_json = json.loads(text_data)
        # extract it
        user = text_data_json['user']
        Msg = text_data_json['Msg']
        Chatroom_id = text_data_json['Chatroom_id']

        # Now send the data back to the group
        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'chatroom',
                'user':user,
                'Msg':Msg,
                'Chatroom_id':Chatroom_id
            }
        )

    @database_sync_to_async
    def SendMessage(self,user):
        sender = models.Profile.objects.get(user__username=user)
        sender = [sender]
        return serializers.serialize('json',sender)

    async def chatroom(self,event):
        user = event['user']  # The sender
        Msg = event['Msg']  # Message
        Chatroom_id = event['Chatroom_id']
        sender = await self.SendMessage(user)
        await self.send(text_data=json.dumps({
            'user': user,
            'Msg': Msg,
            'Chatroom_id':Chatroom_id,
            'sender':sender
        }))