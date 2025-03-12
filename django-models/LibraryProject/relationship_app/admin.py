from django.contrib import admin
from relationship_app.models import Author, Book, Library, Librarian, UserProfile  # Avoid circular import

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(UserProfile) 