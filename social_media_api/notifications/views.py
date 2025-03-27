from django.shortcuts import render
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    """
    Fetches all notifications for the logged-in user.
    Unread notifications are shown first.
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by("-is_read", "-timestamp")

class MarkNotificationReadView(APIView):
    """
    Marks a notification as read.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, notification_id):
        try:
            notification = Notification.objects.get(id=notification_id, recipient=request.user)
            notification.is_read = True
            notification.save()
            return Response({"message": "Notification marked as read."})
        except Notification.DoesNotExist:
            return Response({"error": "Notification not found."}, status=404)
