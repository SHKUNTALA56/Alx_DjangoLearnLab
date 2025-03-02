import django
import os

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author (using filter, not get)
def get_books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)  # ✅ Correct query

# List all books in a specific library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

if __name__ == "__main__":
    print("Books by J.K. Rowling:", list(get_books_by_author("J.K. Rowling")))
    print("Books in Central Library:", list(get_books_in_library("Central Library")))
    print("Librarian of Central Library:", get_librarian_for_library("Central Library"))
