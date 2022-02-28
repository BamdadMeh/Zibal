from django.contrib import admin
from payment.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    list_display = (
        'order_id', 'amount', 'is_paid', 'paid_at',
    )
    list_filter = ('is_paid', 'paid_at', 'created_at')
    search_fields = ('order_id',)
