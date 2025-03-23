# markdown to show how to update the books in the database

from bookshelf.models import Books

retrieved_book = Book.objects.get(title="1984")

#updating the title
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
# Expected output: Title of the book is succesfully updated and saved to the database