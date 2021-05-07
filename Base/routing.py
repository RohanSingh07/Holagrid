from django.urls import re_path,path
from . import consumers
# Just like we have urls inside every new web application
websocket_urlpatterns = [
    path('<room_name>',consumers.HomePage.as_asgi()),
    path('Comments/<room_name>',consumers.CommentPage.as_asgi()),
    path('Explore/<room_name>',consumers.ExplorePage.as_asgi()),
    path('ProfilePage/<room_name>',consumers.ProfilePage.as_asgi()),
    path('Chatroom/<room_name>',consumers.Chatroom.as_asgi()),
    # So here in place of room_name we can type any url and it wil create a chatroom
]