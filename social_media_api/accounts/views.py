from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, Follow
from .serializers import CustomUserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404



from .serializers import CustomUserSerializer, LoginSerializer, FollowSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        if user_to_follow != request.user:
            if request.user.followers.filter(id=user_to_follow.id).exists():
                request.user.followers.remove(user_to_follow)
                return Response({"message": "Unfollowed"}, status=status.HTTP_200_OK)
            else:
                request.user.followers.add(user_to_follow)
                return Response({"message": "Followed"}, status=status.HTTP_200_OK)
        return Response({"message": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)

# Custom Token Authentication View
@api_view(['POST'])
def get_auth_token(request):
    view = ObtainAuthToken.as_view()
    response = view(request)
    if 'token' in response.data:
        return Response({'token': response.data['token'], 'user_id': request.user.id})
    return response

class UnfollowUserView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowSerializer

    def get_object(self):
        follow = get_object_or_404(Follow, user=self.request.user, followed_user_id=self.kwargs["user_id"])
        return follow

class RegisterView(generics.CreateAPIView):
    """User Registration API View"""
    
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]


class LoginView(APIView):
    """User Login API View that returns a token"""

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "user_id": user.id, "username": user.username}, status=status.HTTP_200_OK)
        
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    """User Logout API View that deletes the authentication token"""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.auth.delete()  # Delete the token
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

class UserProfileView(generics.RetrieveUpdateAPIView):
    """API for retrieving and updating user profile"""
    
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user  # Get the logged-in user profile