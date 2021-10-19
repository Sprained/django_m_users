from drf_yasg.utils import swagger_auto_schema
from rest_framework import response
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db import transaction
from drf_yasg import openapi

from users.serializer import UserSerializer
from core.erros import ExceptionMessageBuilder
from users.services import UserService

class UserView(APIView):

  def __init__(self):
    self.userService = UserService()

  @swagger_auto_schema(
    operation_description="partial_update description override",
    request_body=openapi.Schema(
      type=openapi.TYPE_OBJECT,
      properties={
        'nome': openapi.Schema(type=openapi.TYPE_STRING),
        'email': openapi.Schema(type=openapi.TYPE_STRING),
        'phone': openapi.Schema(type=openapi.TYPE_STRING),
        'password': openapi.Schema(type=openapi.TYPE_STRING),
      },
      example={
        'nome': 'teste',
        'email': 'teste@email.com',
        'phone': '81987012741',
        'password': 'teste@123'
      }
    ),
    responses={
      201: '',
      400: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
          'error': openapi.Schema(type=openapi.TYPE_STRING)
        },
        example={
          "error": "Email já cadastrado"
        }
      ),
      422: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
          'nome': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING)),
          'email': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING)),
          'phone': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING)),
          'password': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING)),
        },
        example={
          'nome': [
            'This field is required.'
          ],
          'email': [
            'This field is required.'
          ],
          'phone': [
            'This field is required.'
          ],
          'password': [
            'This field is required.'
          ]
        }
      )
    }
  )
  def post(self, request):
    with transaction.atomic():
      try:
        self.userService.verify_user(request.data['email'])
      except ExceptionMessageBuilder as e:
        return Response(e.message, status=e.status_code)

      serializer = UserSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
  
  def patch(self, request, id):
    with transaction.atomic():
      try:
        user = self.userService.exist_user(id)
      except ExceptionMessageBuilder as e:
        return Response(e.message, status=e.status_code)

      serializer = UserSerializer(user, data=request.data, partial=True)
      if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)

      return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
