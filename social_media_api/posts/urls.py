from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserFeedView, CommentViewSet, LikePostView, UnlikePostView

# Router to automatically generate API endpoints
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),  # Includes all endpoints for posts & comments
    path('feed/', UserFeedView.as_view(), name='user-feed'),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name="like-post"),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name="unlike-post"),
]
