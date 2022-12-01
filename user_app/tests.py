from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User


class RegisterTestCase(APITestCase):

    def test_register(self):
        data = {
            # Correct Dummy data for testing
            'username': 'testcase',
            'email': 'testcase@test.com',
            'password': '123123',
            'confirm_password': '123123'
        }
        response = self.client.post(reverse('register'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return
