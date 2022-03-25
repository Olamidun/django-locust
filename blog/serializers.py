from .models import Post, Comment
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

        extra_kwargs = {
            "id":{
                "read_only": True
            },
        }

class ListPostSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['url', 'title', 'body', 'user']

        extra_kwargs = {
            'url': {'view_name': 'blog:post-detail'},
        }
    