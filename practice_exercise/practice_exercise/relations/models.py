from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        self.title
    
class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(default='')

    def __str__(self):
        return self.user.username