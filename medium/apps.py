from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MediumConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'medium'
    verbose_name = _('Medium')
