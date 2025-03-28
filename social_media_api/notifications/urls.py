from django.urls import path
from .views import NotificationListView, MarkNotificationReadView

urlpatterns = [
    path("", NotificationListView.as_view(), name="notifications-list"),  # Fetch all notifications
    path("<int:notification_id>/read/", MarkNotificationReadView.as_view(), name="mark-notification-read"),  # Mark as read
]
