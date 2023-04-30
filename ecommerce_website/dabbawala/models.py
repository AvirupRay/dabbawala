from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _
from .manager import UserManager

# Create your models here.

class Role(models.Model):
    roles = models.CharField(max_length = 25, null = True)

class User(AbstractUser):
    username = None
    email = models.EmailField(blank = True, null = True, unique=True)
    name = models.CharField(max_length = 100, blank = True, null = True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    # urole = 

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []