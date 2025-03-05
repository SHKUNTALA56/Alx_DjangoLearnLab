from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from .views import (
    home_view,
    list_books,
    LibraryDetailView,
    register_view,
    admin_view,
    librarian_view,
    member_view,
)

urlpatterns = [
    #Home View 
    path('', home_view, name='home'),

    # Book and Library views
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

   
    # Authentication views
    path("register/", register_view, name="register"),
    path('relationship/login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path('accounts/login/', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),


    # Role-based views
    path('admin-dashboard/', admin_view, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_view, name='librarian_dashboard'),
    path('member-dashboard/', member_view, name='member_dashboard'),

     #Include other paths
     
]
