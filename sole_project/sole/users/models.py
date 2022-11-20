from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=False)

    objects = UserManager()

    def get_absolute_url(self):
        # TODO: filter by username
        return reverse("glimpses:list", args=[self.username])