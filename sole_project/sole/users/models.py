from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    username = models.CharField(_("Username"), max_length=150, unique=True)
    email = models.EmailField(_("Email"), unique=True)
    bio = models.TextField(_("Bio"), blank=True, null=False)

    objects = UserManager()

    def get_absolute_url(self):
        # TODO: filter by username
        return reverse("glimpses:list", args=[self.username])
