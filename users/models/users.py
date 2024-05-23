from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField('Никнейм', max_length=60, unique=True)
    email = models.EmailField('Электронная почта', unique=True)
    phone_number 