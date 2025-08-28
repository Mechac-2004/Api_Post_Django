from rest_framework import serializers
from post.models import Post
from .user import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'author']