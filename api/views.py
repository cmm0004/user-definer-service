from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import TwitterUser
from api.helpers.serializers import TwitterUserSerializer, UserSerializer
from django.contrib.auth.models import User

from django.http import Http404
from rest_framework.views import APIView

class TwitterUserList(generics.ListCreateAPIView):
    """
    list all the users, or create new twitter user
    """
    queryset = TwitterUser.objects.all()
    serializer_class = TwitterUserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TwitterUserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    retrieve, update, or delete a twitter user instance
    """
    queryset = TwitterUser.objects.all()
    serializer_class = TwitterUserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
