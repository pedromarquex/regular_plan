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
