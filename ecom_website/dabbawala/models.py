from django.db import models
from django.contrib.auth.models import AbstractUser
# # from django.utils.translation import gettext_lazy as _
from .manager import UserManager

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length = 50)

class Product(models.Model):
    title = models.CharField(max_length = 100, null = True)
    price = models.CharField(max_length = 10, null = True)
    descrption = models.CharField(max_length = 1000, null = True)
    items_img = models.ImageField(upload_to = 'food_items')


class User(AbstractUser):
    username = None
    email = models.EmailField(blank = True, null = True, unique=True)
    name = models.CharField(max_length = 100, blank = True, null = True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []