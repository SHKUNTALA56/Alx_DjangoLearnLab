from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Book

@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        published_date = request.POST.get("published_date")
        isbn = request.POST.get("isbn")

        Book.objects.create(title=title, author=author, published_date=published_date, isbn=isbn)
        return render(request, "bookshelf/book_list.html", {"books": Book.objects.all()})

    return render(request, "bookshelf/book_form.html")

@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.title = request.POST.get("title", book.title)
        book.author = request.POST.get("author", book.author)
        book.published_date = request.POST.get("published_date", book.published_date)
        book.isbn = request.POST.get("isbn", book.isbn)
        book.save()
        return render(request, "bookshelf/book_list.html", {"books": Book.objects.all()})

    return render(request, "bookshelf/book_form.html", {"book": book})

@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return render(request, "bookshelf/book_list.html", {"books": Book.objects.all()})
