from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .serializers import GroupSerializer, UserSerializer, CommentSerializer
from .models import CommentModel

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):

    # API endpoint that allows users to be viewed and edited
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer
    permission_class = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    #API endpoint to allow groupd to be viewed and edited
    queryset = User.objects.all().order_by('username')
    serializer_class = GroupSerializer
    permission_class = [permissions.IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):

    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

    @action(detail=True, methods=['post'])
    def flag(self, request, pk=None):
        comment = self.get_object
        comment.flagged = True
        comment.save()
        return Response({'Message': 'comment flagged for moderation'}, status=status.HTTP_200_OK)
