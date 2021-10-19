from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db import transaction

from users.serializer import RegisterUserSerializer

class UserView(APIView):

  def post(self, request):
    with transaction.atomic():
      serializer = RegisterUserSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)