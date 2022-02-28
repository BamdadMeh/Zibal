from django.urls import path
from payment import views

app_name = 'payment'


urlpatterns = (

    path(
        '<int:order_id>/<int:amount>/',
        views.OrderPayment.as_view(),
        name='order_payment'
    ),
    path(
        'verify/',
        views.OrderPaymentVerify.as_view(),
        name='order_payment_verify'
    ),

)
