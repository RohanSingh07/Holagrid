from django.urls import re_path,path
from . import consumers
# Just like we have urls inside every new web application
websocket_urlpatterns = [
    path('<room_name>',consumers.SignPage2.as_asgi())]