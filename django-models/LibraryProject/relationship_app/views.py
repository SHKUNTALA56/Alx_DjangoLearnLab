from django.shortcuts import render
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView


from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Library

# ✅ Function-based view to list books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books}) 

# ✅ Class-based view for Library details

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
  

    
