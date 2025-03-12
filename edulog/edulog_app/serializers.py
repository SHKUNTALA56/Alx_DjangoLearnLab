from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import AttendanceLog

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwags = {"password": {"write_only": True} }

    def create(self, validated_data):
        """Ensure password is hashed before saving."""
        password = validated_data.pop("password", None)
        user = User(**validated_data)
        if password:
            user.set_password(password)  # Hash the password
        user.save()
        return user

class AttendanceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceLog
        fields = ["id", "user", "timestamp", "action"]