from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions

from api.models import Users, Followers
from api.serializers import UserSerializer, UserDetailSerializer
import random

class UserList(APIView):
    """
    List all users.
    """               
    def get(self, request, offset=0, limit=10, format=None):
        if offset is None:
            offset = 0
        if limit is None:
            limit = 10
        try:
            users = Users.objects.all()[offset:limit]
            count = Users.objects.all()[offset:limit].count()
            total_count = Users.objects.count()
            serializer = UserSerializer(users, many=True)
            response = Response()
            response['count'] = count
            response['total_count'] = total_count
            response.data = serializer.data
            response.status = status.HTTP_200_OK 
            return response
        except Users.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST) 

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
        if 'token' not in request.session: 
            return Response(status=status.HTTP_400_BAD_REQUEST)
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

    def delete(self, request, pk, format=None):
        if 'token' not in request.session or 'userId' not in request.session: 
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            Users.objects.filter(pk=pk).delete()
            return Response(status=status.HTTP_200_OK)
        except Users.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)   

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
            request.session['userId'] = user.id
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Users.DoesNotExist:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        """
        logout.
        """
        try:
            del request.session['token']
            del request.session['userId']
        except KeyError:
            pass     
        return Response(status=status.HTTP_200_OK)

class Follow(APIView):
    """
    follow a valid user.
    """
    def post(self, request, pk, format=None):
        if 'token' not in request.session or 'userId' not in request.session: 
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            follower = Users.objects.get(pk=request.session['userId'])
            follow = Users.objects.get(pk=pk)    
            f = Followers(user_id=follow, followed_by_id=follower)
            f.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Users.DoesNotExist:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

    """
    unfollow a followed user.
    """
    def delete(self, request, pk, format=None):
        if 'token' not in request.session or 'userId' not in request.session: 
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            follower = Users.objects.get(pk=request.session['userId'])
            unfollow = Users.objects.get(pk=pk)    
            query = Followers.objects.filter(user_id=unfollow, followed_by_id=follower)
            query.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except follower.DoesNotExist or unfollow.DoesNotExist or query.DoesNotExist:
            raise Http404      




        
