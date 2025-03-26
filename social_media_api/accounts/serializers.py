from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


CustomUser = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    """Serializer for retrieving user details and registration"""
    
    password = serializers.CharField(write_only=True, required=True)  # Ensure password is write-only
    followers = serializers.PrimaryKeyRelatedField(many=True, queryset=CustomUser.objects.all(), required=False)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture', 'followers']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Override create method to hash password and generate token"""
        followers = validated_data.pop('followers', [])  # Extract followers if provided
        user = get_user_model().objects.create_user(**validated_data)
        
        user.followers.set(followers)  # Set followers if provided
        Token.objects.create(user=user)  # Create a token for new users
        return user
    
class LoginSerializer(serializers.Serializer):
    """Serializer for user login"""
    
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
