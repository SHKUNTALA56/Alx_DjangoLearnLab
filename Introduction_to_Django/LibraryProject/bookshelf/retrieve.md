# Retrieving a Book Instance" 
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="1984")

# Display book details
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")