# Deleting a Book Instance" 
from bookshelf.models import Book  

# Retrieve the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm the deletion by retrieving all books
books = Book.objects.all()
print(list(books))  # This should return an empty list if deletion was successful
