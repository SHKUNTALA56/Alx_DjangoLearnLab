from django.apps import AppConfig
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse


class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'


def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome, Admin!")

@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome, Librarian!")

@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome, Member!")
