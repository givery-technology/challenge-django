from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Users
import datetime

class UserTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new user object.
        """
        url = reverse('user-create')
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

class ShowUser(APITestCase):
    def test_show_user(self):
        u = Users(id=5, username='testing5', email='testing5@testing.com', password='password')
        u.save()
        url = reverse('show-user', args=[5])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_user_not_present(self):
        url = reverse('show-user', args=[5])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class UpdateUser(APITestCase):
    def test_update_username_without_login(self):   
        u = Users(id=6, username='testing6', email='testing6@testing.com', password='password')
        u.save()
        url = reverse('show-user', args=[6])
        data = {'username': 'user6'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)     

    def test_update_user_with_login(self):   
        u = Users(id=7, username='testing7', email='testing7@testing.com', password='password', birthday='1997-04-17')
        u.save()

        url = reverse('login')
        data = {'email': 'testing7@testing.com', 'password': 'password'}
        response = self.client.post(url, data, format='json')

        if self.assertEqual(response.status_code, status.HTTP_200_OK):
            url = reverse('show-user', args=[7])
            data = {'username': 'user7', 'email':'user7@testing.com', 'password':'password7', 'birthday':'1994-04-13', 'company':'Givery', 'location':'Tokyo'}
            response = self.client.put(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)     
            self.assertEqual(Users.objects.get().username, 'user7')
            self.assertEqual(Users.objects.get().email, 'user7@testing.com') 
            self.assertEqual(Users.objects.get().password, 'password7')
            self.assertEqual(Users.objects.get().birthday, datetime.date(1994, 4, 13))   
            self.assertEqual(Users.objects.get().company, 'Givery')   
            self.assertEqual(Users.objects.get().location, 'Tokyo')   

class DeleteUser(APITestCase):
    def test_delete_username_without_login(self):   
        u = Users(id=8, username='testing8', email='testing8@testing.com', password='password')
        u.save()
        url = reverse('show-user', args=[8])
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)     

    def test_delete_user_with_login(self):   
        u = Users(id=9, username='testing9', email='testing9@testing.com', password='password', birthday='1997-04-17')
        u.save()

        url = reverse('login')
        data = {'email': 'testing9@testing.com', 'password': 'password'}
        response = self.client.post(url, data, format='json')

        if self.assertEqual(response.status_code, status.HTTP_200_OK):
            url = reverse('show-user', args=[9])
            response = self.client.delete(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)       

class FollowUser(APITestCase):
    def test_follow_user_without_login(self):
        u = Users(id=10, username='testing10', email='testing10@testing.com', password='password', birthday='1997-04-17')
        u.save()
        u = Users(id=11, username='testing11', email='testing11@testing.com', password='password', birthday='1997-04-17')
        u.save()

        url = reverse('follow', args=[11])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_follow_user_with_login(self):
        u = Users(id=12, username='testing12', email='testing12@testing.com', password='password', birthday='1997-04-17')
        u.save()
        u = Users(id=13, username='testing13', email='testing13@testing.com', password='password', birthday='1997-04-17')
        u.save()

        url = reverse('login')
        data = {'email': 'testing12@testing.com', 'password': 'password'}
        response = self.client.post(url, data, format='json')

        if self.assertEqual(response.status_code, status.HTTP_200_OK):
            url = reverse('follow', args=[13])
            response = self.client.post(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK) 

class UnFollowUser(APITestCase):
    def test_unfollow_user_without_login(self):
        u = Users(id=14, username='testing14', email='testing14@testing.com', password='password', birthday='1997-04-17')
        u.save()
        u = Users(id=15, username='testing15', email='testing15@testing.com', password='password', birthday='1997-04-17')
        u.save()

        url = reverse('follow', args=[15])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unfollow_user_with_login_without_followed_fail(self):
        u = Users(id=16, username='testing16', email='testing16@testing.com', password='password', birthday='1997-04-17')
        u.save()
        u = Users(id=17, username='testing17', email='testing17@testing.com', password='password', birthday='1997-04-17')
        u.save()

        url = reverse('login')
        data = {'email': 'testing16@testing.com', 'password': 'password'}
        response = self.client.post(url, data, format='json')

        if self.assertEqual(response.status_code, status.HTTP_200_OK):
            url = reverse('follow', args=[17])
            response = self.client.post(url)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unfollow_user_with_login_with_followed_success(self):
        u = Users(id=18, username='testing18', email='testing18@testing.com', password='password', birthday='1997-04-17')
        u.save()
        u = Users(id=19, username='testing19', email='testing19@testing.com', password='password', birthday='1997-04-17')
        u.save()

        url = reverse('login')
        data = {'email': 'testing18@testing.com', 'password': 'password'}
        response = self.client.post(url, data, format='json')

        if self.assertEqual(response.status_code, status.HTTP_200_OK):
            url = reverse('follow', args=[19])
            response = self.client.post(url)
            if self.assertEqual(response.status_code, status.HTTP_200_OK):        
                url = reverse('follow', args=[19])
                response = self.client.delete(url)
                self.assertEqual(response.status_code, status.HTTP_200_OK)

class Pager(APITestCase):
    def test_pager_without_param(self):
        u = Users(id=20, username='testing20', email='testing20@testing.com', password='password', birthday='1997-04-17')
        u.save()
        u = Users(id=21, username='testing21', email='testing21@testing.com', password='password', birthday='1991-04-17')
        u.save()
        u = Users(id=22, username='testing22', email='testing22@testing.com', password='password', birthday='1992-04-17')  
        u.save()
        u = Users(id=23, username='testing23', email='testing23@testing.com', password='password', birthday='1993-04-17')
        u.save()
        u = Users(id=24, username='testing24', email='testing24@testing.com', password='password', birthday='1994-04-17')
        u.save()
        u = Users(id=25, username='testing25', email='testing25@testing.com', password='password', birthday='1995-04-17')
        u.save()
        u = Users(id=26, username='testing26', email='testing26@testing.com', password='password', birthday='1996-04-17')
        u.save()
        u = Users(id=27, username='testing27', email='testing27@testing.com', password='password', birthday='1991-04-17')
        u.save()
        u = Users(id=28, username='testing28', email='testing28@testing.com', password='password', birthday='1990-04-17')
        u.save()
        u = Users(id=29, username='testing29', email='testing29@testing.com', password='password', birthday='1990-04-13')
        u.save()
        u = Users(id=30, username='testing30', email='testing30@testing.com', password='password', birthday='1991-04-13')
        u.save()

        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  
        self.assertEqual(response['count'], '10')
        self.assertEqual(response['total_count'], '11')
        self.assertEqual(response.data[0]['username'], 'testing20')

        url = reverse('user-list', kwargs={'offset':5})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['count'], '5')
        self.assertEqual(response['total_count'], '11')
        self.assertEqual(response.data[0]['username'], 'testing25')

        url = reverse('user-list', kwargs={'offset': 0, 'limit':5})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['count'], '5')
        self.assertEqual(response['total_count'], '11')
        self.assertEqual(response.data[0]['username'], 'testing20')

        url = reverse('user-list', kwargs={'offset': 2, 'limit':5})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['count'], '3')
        self.assertEqual(response['total_count'], '11')
        self.assertEqual(response.data[0]['username'], 'testing22')

        url = reverse('user-list', kwargs={'limit':5})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['count'], '5')
        self.assertEqual(response['total_count'], '11')
        self.assertEqual(response.data[0]['username'], 'testing20')

        # offset = 0
        # limit = 5
        # order_by = 
        # order = 














                          
