from django.urls import path
from .views import FollowUserView, get_auth_token, RegisterView, LoginView, LogoutView, UserProfileView

urlpatterns = [
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('api/token/', get_auth_token, name='get-auth-token'),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/auth/logout/', LogoutView.as_view(), name='logout'),
    path('api/auth/profile/', UserProfileView.as_view(), name='profile'),
]
