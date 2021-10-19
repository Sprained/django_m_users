from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.models import User

class UserSerializer(serializers.ModelSerializer):
  nome = serializers.CharField(max_length=100)
  email = serializers.EmailField(max_length=100)
  phone = serializers.CharField(max_length=11)
  password = serializers.CharField(max_length=100)

  class Meta:
    model = User
    fields = ['nome', 'email', 'phone', 'password']

  def create(self, validated_data):
    user = User.objects.db_manager('erp').create(
      nome = validated_data['nome'],
      password = make_password(
        validated_data['password']
      ),
      email = validated_data['email'],
      phone = validated_data['phone']
    )
    return user

  def update(self, instance, validated_data):
    if 'nome' in validated_data:
      instance.nome = validated_data['nome']
    if 'password' in validated_data:
      instance.password = make_password(
        validated_data['password']
      )
    if 'email'  in validated_data:
      instance.email = validated_data['email']
    if 'phone'  in validated_data:
      instance.phone = validated_data['phone']
    
    instance.save()

    return instance