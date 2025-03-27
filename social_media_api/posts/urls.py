from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserFeedView, CommentViewSet

# Router to automatically generate API endpoints
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),  # Includes all endpoints for posts & comments
    path('feed/', UserFeedView.as_view(), name='user-feed'),

]
