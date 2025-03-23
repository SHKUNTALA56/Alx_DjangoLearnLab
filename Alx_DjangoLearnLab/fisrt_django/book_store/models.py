from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
