# from passlib.hash import pbkdf2_sha256

from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Users
from api.serializers import UserSerializer, UserDetailSerializer
from api.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework import permissions
from django.core.exceptions import ObjectDoesNotExist
import random

# from django.db.models import Q

class UserList(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

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

    # def put(self, request, pk, format=None):
    #     user = self.get_object(pk)
    #     serializer = UserSerializer(user, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
            print("givery")
            print(request)
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

    # def delete(self, request, pk, format=None):
    #     user = self.get_object(pk)
    #     user.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

# class UserList(generics.ListAPIView):
#     """
#     List all users, or create a new user.
#     """
#     # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
#     queryset = Users.objects.all()
#     serializer_class = UserSerializer

# class UserCreate(generics.CreateAPIView):
#     """
#     List all users, or create a new user.
#     """
#     # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
#     queryset = Users.objects.all()
#     serializer_class = UserSerializer    


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Retrieve, update or delete a user instance.
#     """
#     # if "token" in request.session:
#     #     # permission_classes = (IsOwnerOrReadOnly,)
#     queryset = Users.objects.all()
#     serializer_class = UserSerializer


# class UserList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Users.objects.all()
#     serializer_class = UserSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class UserDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Users.objects.all()
#     serializer_class = UserSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)

