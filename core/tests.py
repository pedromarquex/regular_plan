from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import MyUser


class UserTest(APITestCase):
    def test_create_user(self):
        """
        ensure we can create a user
        """
        url = '/register/'
        user_data = {
            "name": "Atila Lamarino",
            "user": {
                "username": "oatila",
                "password": "atilahatescovid"
            }
        }

        response = self.client.post(url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_user = MyUser.objects.get(user__username="oatila")
        self.assertEqual(response.data['id'], str(created_user.id))

    def test_create_user_without_name(self):
        """
        ensure we can't create a user without a name
        """
        url = '/register/'
        user_data = {
            "user": {
                "username": "oatila",
                "password": "atilahatescovid"
            }
        }

        response = self.client.post(url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login(self):
        """
        ensure we can authenticate a user
        """
        url = '/auth/'
        login_data = {
            "username": "oatila",
            "password": "atilahatescovid"
        }
        User.objects.create_user(**login_data)
        response = self.client.post(url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_fail_login(self):
        """
        ensure we can't authenticate a user that does not exists
        """
        url = '/auth/'
        login_data = {
            "username": "oatila",
            "password": "atilahatescovid"
        }
        response = self.client.post(url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
