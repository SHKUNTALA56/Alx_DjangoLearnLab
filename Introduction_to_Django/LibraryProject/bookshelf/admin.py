from django.contrib import admin

from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these fields in the list view
    search_fields = ('title', 'author')  # Add search functionality
    list_filter = ('publication_year',)  # Add filter options for publication year
