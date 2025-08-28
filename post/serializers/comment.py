from rest_framework import serializers
from post.models import Comment
from .user import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post_title = serializers.CharField(source='post.title', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'author', 'post_title']