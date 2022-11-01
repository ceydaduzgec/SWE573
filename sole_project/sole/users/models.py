from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    """

    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)
