from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CustomAuthConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cnab_reader.custom_auth"
    verbose_name = _("autenticação")
