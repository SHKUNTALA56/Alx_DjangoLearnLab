from django.contrib import admin
from django.urls import path, include
from relationship_app import views  # Import the views module
from relationship_app.views import librarian_dashboard_view

urlpatterns = [
    path('', views.home_view, name='home'),  # Home page
    path('admin/', admin.site.urls),  # Admin panel

    # Book-related paths
    path('books/', views.list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view

    # Role-based views
    path('admin-page/', views.admin_view, name='admin_view'),
    path('librarian-page/', views.librarian_view, name='librarian_view'),
    path('member-page/', views.member_view, name='member_view'),
    path('librarian-dashboard/', views.librarian_dashboard_view, name='librarian_dashboard'),

    # Include authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),

    # Including additional app-specific URLs
    path('relationship/', include('relationship_app.urls')),
]
