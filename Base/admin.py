from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Posts)
admin.site.register(models.Comments)
admin.site.register(models.Profile)
admin.site.register(models.Messages)
admin.site.register(models.Chatroom)
admin.site.register(models.Stories)