# Updating a Book Title" 
from bookshelf.models import Book  

# Retrieve the book instance
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"

# Save the changes
book.save()

print(f"Updated Title: {book.title}")
# Confirm the update