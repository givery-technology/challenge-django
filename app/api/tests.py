from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Users

class UserTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new user object.
        """
        url = reverse('user-list')
        data = {'username': 'testing1', 'email': 'testing1@testing.com', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Users.objects.count(), 1)
        self.assertEqual(Users.objects.get().username, 'testing1')

        data = {'username': 'testing2', 'email': 'testing2@testing.com', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Users.objects.count(), 2)

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)      

class LoginTests(APITestCase):
    def test_login(self):
        u = Users(username='testing3', email='testing3@testing.com', password='password')
        u.save()
        url = reverse('login')
        data = {'email': 'testing3@testing.com', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  

class LogoutTests(APITestCase):
    def test_logout(self) :
        u = Users(username='testing4', email='testing4@testing.com', password='password')
        u.save()
        url = reverse('login')
        data = {'email': 'testing4@testing.com', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        url = reverse('logout')   
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
