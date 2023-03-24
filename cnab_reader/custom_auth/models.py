from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.db import models
from django.utils.translation import gettext_lazy as _

from cnab_reader.custom_auth.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(_("nome"), max_length=150)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # type: ignore

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name or self.email


class CustomGroup(Group):
    """
    Criado apenas para fazer proxy e manter o Group na mesma app do CustomUser.
    """

    class Meta:
        proxy = True
        verbose_name = _("grupo")
        verbose_name_plural = _("grupos")
