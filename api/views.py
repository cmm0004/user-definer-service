from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import TwitterUser
from api.helpers.serializers import TwitterUserSerializer

from django.http import Http404
from rest_framework.views import APIView

class TwitterUserList(generics.ListCreateAPIView):
    """
    list all the users, or create new twitter user
    """
    queryset = TwitterUser.objects.all()
    serializer_class = TwitterUserSerializer

class TwitterUserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    retrieve, update, or delete a twitter user instance
    """
    queryset = TwitterUser.objects.all()
    serializer_class = TwitterUserSerializer