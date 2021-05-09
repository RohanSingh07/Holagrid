"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
import django
import os

from django.core.asgi import get_asgi_application
from channels.layers import get_channel_layer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
application = get_asgi_application()
channel_layer = get_channel_layer()