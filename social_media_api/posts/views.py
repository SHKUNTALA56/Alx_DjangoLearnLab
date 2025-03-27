from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, filters, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Post, Comment,Like
from .serializers import PostSerializer, CommentSerializer
from accounts.models import CustomUser, Follow  # Import the user model
from rest_framework.permissions import IsAuthenticated
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification


user = CustomUser

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

class UserFeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Retrieve posts from users the authenticated user follows."""
        user = request.user

        # Get the list of users the authenticated user follows
        following_users = user.following.all()

        # Get posts from those users, ordered by most recent
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        serializer = PostSerializer(posts, many=True)
        return Response({"feed": serializer.data})      


class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            return Response({"message": "Post liked successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "You have already liked this post"}, status=status.HTTP_400_BAD_REQUEST)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()

        if like:
            like.delete()
            return Response({"message": "Post unliked successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "You haven't liked this post"}, status=status.HTTP_400_BAD_REQUEST)