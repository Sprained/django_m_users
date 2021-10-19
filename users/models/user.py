from django.db import models

class User(models.Model):
  nome = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  password = models.CharField(max_length=100)
  active = models.BooleanField(default=True)
  phone = models.CharField(max_length=11)

  class Meta:
    db_table = 'user'