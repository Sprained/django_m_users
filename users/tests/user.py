from django.test.testcases import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class RegisterUserSerializer(TestCase):
  databases = '__all__'

  def test_create_user_success(self):
    obj = {
      'nome': 'test',
      'email': 'teste@email.com',
      'password': 'teste@123',
      'phone': '12345678901'
    }

    url = reverse('user')

    response = self.client.post(url, data=obj, format='json')

    self.assertEqual(response.status_code, status.HTTP_201_CREATED)