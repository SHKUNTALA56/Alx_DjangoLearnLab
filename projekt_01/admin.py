from django.contrib import admin
from .models import YourModel, Book  # Import models

# Registering YourModel with customization
@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')  # Customize columns
    search_fields = ('name',)  # Add a search bar
    list_filter = ('created_at',)  # Add filters

# Registering Book model normally
admin.site.register(Book)
