from rest_framework import serializers

from .models import Posts
from users.models import Account
# Serialzer for Posts
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['user', 'File1','File1Type','File2','File2Type','File3','File3Type','File4','File4Type','File5','File5Type','File6','File6Type','File7','File7Type',
                  'File8','File8Type','File9','File9Type','File10','File10Type','Description','Filter','Comments','Likes','Liked_by','slug','Date','Time'
        ]

# Serializer for Authentication
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=['phone','username','email','password']

