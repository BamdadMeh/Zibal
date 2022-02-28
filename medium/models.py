from django.db import models
from django.utils.translation import gettext_lazy as _


class MediumReport(models.Model):

    message = models.TextField(_('message'))
    sent_at = models.DateTimeField(_('sent date'), auto_now_add=True)
    medium = models.CharField(_("medium's name"), max_length=255)
    receiver = models.CharField(_('receiver'), max_length=255)

    class Meta:
        verbose_name = _('medium report')
        verbose_name_plural = _('medium reports')

    def __str__(self):
        return f'{self.pk}'
