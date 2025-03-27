from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    """Serializer for Post model"""
    
    author = serializers.ReadOnlyField(source='author.username')  # Show username instead of ID

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model"""

    author = serializers.ReadOnlyField(source='author.username')  # Show username instead of ID
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())  # Reference Post by ID

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
