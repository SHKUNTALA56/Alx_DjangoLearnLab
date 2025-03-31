from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_groups",  # Fix name conflicts
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",  # Fix name conflicts
        blank=True
    )

    def __str__(self):
        return self.username

class Follow(models.Model):
    follower = models.ForeignKey(
        CustomUser, related_name="following", on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        CustomUser, related_name="followers", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')  # Prevent duplicate follows

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"
