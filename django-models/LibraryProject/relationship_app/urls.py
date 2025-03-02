from django.urls import path
from .views import list_books, LibraryDetailView
from .views import register_view, login_view, logout_view, list_books
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import views from the current app
urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
       path('register/', register_view, name='register'),
]
   

urlpatterns = [
    # Registration view
    path("register/", views.register, name="register"),
    
    # Login view
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    
    # Logout view
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]


