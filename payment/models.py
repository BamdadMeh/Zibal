from django.db import models
from django.utils.translation import gettext_lazy as _


class Payment(models.Model):

    order_id = models.PositiveBigIntegerField(_('order number'))
    amount = models.PositiveBigIntegerField(_('price'))
    track_id = models.CharField(
        _('unique payment ID'),
        max_length=128,
        unique=True,
        null=True,
        blank=True
    )
    is_paid = models.BooleanField(_('status paid'), default=False)
    paid_at = models.DateTimeField(_('date paid'), null=True, blank=True)
    ref_number = models.CharField(
        _('refrence payment number'),
        max_length=255,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(_('date created'), auto_now_add=True)

    class Meta:
        verbose_name = _('payment')
        verbose_name_plural = _('payments')

    def __str__(self):
        return f'{self.order_id} - {self.amount}'
