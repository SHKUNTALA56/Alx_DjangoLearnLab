from django.core.exceptions import PermissionDenied

def is_admin(user):
    if not user.is_authenticated or user.userprofile.role != 'Admin':
        raise PermissionDenied

def is_librarian(user):
    if not user.is_authenticated or user.userprofile.role != 'Librarian':
        raise PermissionDenied

def is_member(user):
    if not user.is_authenticated or user.userprofile.role != 'Member':
        raise PermissionDenied
