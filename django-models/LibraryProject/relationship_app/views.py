from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import DetailView
from django.contrib.auth.decorators import user_passes_test
from .models import Book, Library, UserProfile


# ✅ Home Page View
def home_view(request):
    return render(request, 'relationship_app/home.html')


# ✅ Function-based view to list books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# ✅ Class-based view for Library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# ✅ User Registration View
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Ensure a UserProfile is created only if it doesn't exist
            user_profile, created = UserProfile.objects.get_or_create(user=user, defaults={'role': 'Member'})

            if not created:
                messages.error(request, "User profile already exists!")
                return redirect("register")

            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})



# ✅ User Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


# ✅ User Logout View
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login after logout


# ✅ Helper Functions to Check User Role
def is_admin(user):
    return user.is_authenticated and getattr(user, 'userprofile', None) and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and getattr(user, 'userprofile', None) and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and getattr(user, 'userprofile', None) and user.userprofile.role == 'Member'


# ✅ Admin Dashboard
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_dashboard.html')


# ✅ Librarian Dashboard
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_dashboard.html')


# ✅ Member Dashboard
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_dashboard.html')



from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def librarian_dashboard_view(request):
    return render(request, 'relationship_app/librarian_dashboard.html')

