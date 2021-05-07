from channels.generic.websocket import AsyncWebsocketConsumer
import json
from . import models
from channels.db import database_sync_to_async
from django.contrib.auth.models import User


class SignPage2(AsyncWebsocketConsumer):

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
        username = text_data_json['username']
        # Now send the data back to the group
        await self.channel_layer.group_send(
            self.room_group_name,{
                'type':'Signup_Calls',
                'username':username,

            }
        )

