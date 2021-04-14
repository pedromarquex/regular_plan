from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from core.models import MyUser


class PlanTest(APITestCase):
    def test_list_plans(self):
        """
        ensure we can list all plans with a authenticated user
        """
        user_data = {
            "username": "oatila",
            "password": "atilahatescovid"
        }
        user = User.objects.create_user(**user_data)
        my_user_data = {
            "name": "Atila",
            "user": user
        }
        MyUser.objects.create(**my_user_data)
        auth_url = '/auth/'
        auth_response = self.client.post(auth_url, user_data, format='json')

        url = '/plans/'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + auth_response.data['access'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
