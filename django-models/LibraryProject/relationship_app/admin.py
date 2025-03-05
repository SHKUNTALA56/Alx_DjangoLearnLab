from django.contrib import admin

from django.contrib import admin
from django.contrib import admin
from .models import UserProfile



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')  # Displays the username and role in the admin panel
    search_fields = ('user__username', 'role')  # Enables searching by username and role
    list_filter = ('role',)  # Adds a filter for roles in the admin panel

# If you have more models, register them below
from django.contrib import admin
from .models import Library, Book  # Import your models

admin.site.register(Library)
admin.site.register(Book)



