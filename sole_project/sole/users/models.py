from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    username = models.CharField(
        _("Username"),
        max_length=150,
        unique=True,
        blank=False,
        validators=[
            RegexValidator(
                r"^[a-z0-9._]{3,}$",  # Only lowercase English letters, period and underscore characters are allowed. Minimum length is three characters.
                _(
                    "Username is invalid. Only lowercase English letters, period and underscore characters are allowed. Minimum length is three characters."
                ),
            )
        ],
    )
    email = models.EmailField(_("Email"), unique=True, blank=False)
    bio = models.TextField(_("Bio"), blank=True, null=False)

    objects = UserManager()

    def get_absolute_url(self):
        return reverse("glimpses:list", args=[self.username])

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
