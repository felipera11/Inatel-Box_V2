# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    matricula = models.PositiveIntegerField(unique=True)
    nome = models.CharField(max_length=150)

    USERNAME_FIELD = 'matricula'
    REQUIRED_FIELDS = ['email']
