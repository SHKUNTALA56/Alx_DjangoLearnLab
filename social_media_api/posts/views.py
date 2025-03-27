from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# Custom permission to allow only the author to edit or delete
class IsAuthorOrReadOnly(permissions.BasePermission):
    """Custom permission to allow only the post/comment author to edit/delete"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # Allow GET, HEAD, OPTIONS
            return True
        return obj.author == request.user  # Allow edit/delete only if user is the author


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet for Post model with CRUD operations"""
    
    queryset = Post.objects.all().order_by('-created_at')  # Get all posts, latest first
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]  # Require authentication & author control

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        """Automatically set the post author to the logged-in user"""
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet for Comment model with CRUD operations"""
    
    queryset = Comment.objects.all().order_by('-created_at')  # Get all comments, latest first
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]  # Require authentication & author control

    def perform_create(self, serializer):
        """Automatically set the comment author to the logged-in user"""
        serializer.save(author=self.request.user)

