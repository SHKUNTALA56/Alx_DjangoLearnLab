# markdown to illustrate deleition of a retrieved book

from bookshelf.models import Books

retrieved_book = Book.objects.get(title="Nineteen Eighty-Four")
retrived_book.delete()
# Expected Output: The book instance is successfully deleted from the database.

#confirming the deletion of the book

all_books = Books.objects.all()
print(all_books)

# Expected output": <QuerySet []> or similar output showing no books in the database