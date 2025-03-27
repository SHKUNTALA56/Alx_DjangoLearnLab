from django.urls import path
from .views import FollowUserView,UnfollowUserView, get_auth_token, RegisterView, LoginView, LogoutView, UserProfileView



urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('token/', get_auth_token, name='get-auth-token'),
]
