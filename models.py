from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import UserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    user_profile_image = models.TextField(blank=True, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()
    
    