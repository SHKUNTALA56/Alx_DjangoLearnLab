# CRUD Operations in Django Shell" 
from bookshelf.models import Book  

# Create a new book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Confirm creation
print(book)

# Retrieve the created book
retrieved_book = Book.objects.get(title="1984")

# Display book details
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)
# Retrieve the book instance
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm update
print(book.title)
# Retrieve and delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
books = Book.objects.all()
print(list(books))  # Should return an empty list
