from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import AttendanceLog
from .serializers import AttendanceLogSerializer, UserSerializer
from .permissions import IsAdmin
from rest_framework.views import APIView
from django.contrib.auth import authenticate

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed and edited"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class StudentLoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_staff:
                return Response({"You cannot login as an admin!"}, status=status.HTTP_403_FORBIDDEN)
            token, _ = token.objects.get_or_create(user=user)

            return Response({
                "token": token.key,
                "message": "Login successful!",
                "redirect_url": "/student-dashboard/" # redirect to dashboard if authenticated
            })

        return Response({"Invalid credentials!Please try again!"}, status=status.HTTP_401_UNAUTHORIZED)
    
class AttendanceLogViewSet(viewsets.ModelViewSet):
    """API endpoint to manage attendance logs"""
    queryset = AttendanceLog.objects.all()
    serializer_class = AttendanceLogSerializer
    permission_classes = [IsAdmin]

    @action(detail=False, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def login_log(self, request):
        """Log student login"""
        AttendanceLog.objects.create(user=request.user, action="login")
        return Response({"message": "Login recorded."}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def logout_log(self, request):
        """Log student logout"""
        AttendanceLog.objects.create(user=request.user, action="logout")
        return Response({"message": "Logout recorded."}, status=status.HTTP_201_CREATED)
