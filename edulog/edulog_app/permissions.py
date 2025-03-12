from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Custom permission to allow only admin users to access the view.
    """

    def has_permission(self, request, view):
        print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")  # Debugging
        print(f"User Role: {getattr(request.user, 'role', None)}")  # Debugging
        
        return request.user.is_authenticated and getattr(request.user, 'role', None) == 'admin'
