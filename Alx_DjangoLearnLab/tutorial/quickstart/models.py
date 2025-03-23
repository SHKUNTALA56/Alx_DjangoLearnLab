from django.db import models

# Create your models here.
class CommentModel(models.Model):
    text = models.TextField(null=True)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    flagged = models.BooleanField(default=False)

    def __str__(self):
        return f"comment by {self.author}: {self.text[:50]}"