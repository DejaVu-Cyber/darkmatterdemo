from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=20)
    collection_manager = models.BooleanField(default=False)
# Create your models here.

