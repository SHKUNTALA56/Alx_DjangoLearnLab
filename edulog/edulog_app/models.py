from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('student', 'Student'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='student')
    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

class AttendanceLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=50, choices=[('login', 'Login'), ('logout', 'Logout')])

    def __str__(self):
        return f"{self.user.username} - {self.action} at {self.timestamp} "