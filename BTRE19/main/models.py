from django.contrib.auth.models import AbstractUser
from django.db import models

class users(AbstractUser):
    phone = models.CharField(max_length=11, unique=True)
    def __str__(self):
        return self.username
