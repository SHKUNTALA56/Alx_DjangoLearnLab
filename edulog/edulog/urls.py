from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from edulog_app import views

router = routers.DefaultRouter()
router.register(r'attendance', views.AttendanceLogViewSet, basename='attendnace')
router.register(r'users', views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),  
    path('auth-users/', include('rest_framework.urls', namespace='rest_framework')),
    path("student-login/", views.StudentLoginView.as_view(), name="student-login"),
]   