from .models import post
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  # Display the username instead of the user ID
    class Meta:
        model = post.comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = post
        fields = ['id', 'author', 'content', 'created_at', 'updated_at']


