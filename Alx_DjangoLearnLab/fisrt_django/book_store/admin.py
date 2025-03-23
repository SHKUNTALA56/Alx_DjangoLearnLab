from django.contrib import admin
from .models import Products

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at')  # Adjusted fields
    search_fields = ('name', 'category')  # Allows searching by name and category
    list_filter = ('category', 'created_at')  # Enables filtering by category and date
    ordering = ('-created_at',)  # Orders products by newest first

admin.site.register(Products, ProductsAdmin)
