from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions

from api.models import Users
from api.serializers import UserSerializer, UserDetailSerializer
import random

class UserList(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserCreate(APIView):
    """
    create a new user.
    """
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)  
        if 'email' not in request.data:
            request.data['email'] = user.email
        if 'username' not in request.data:
            request.data['username'] = user.username
        if 'password' not in request.data:
            request.data['password'] = user.password
        serializer = UserDetailSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        """
        login.
        """
        email = request.data['email']
        password = request.data['password']
        try:
            user = Users.objects.get(email=email, password=password)
            serializer = UserDetailSerializer(user)
            token = '%32x' % random.getrandbits(16*8)
            request.session['token'] = token
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Users.DoesNotExist:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        """
        logout.
        """
        try:
            del request.session['token']
        except KeyError:
            pass     
        return Response(status=status.HTTP_200_OK)
