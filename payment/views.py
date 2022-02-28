from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from payment.models import Payment
from payment.services import ZibalPaymentRequest, ZibalPaymentVerification
from payment.send_message import send_message


@method_decorator(csrf_exempt, name='dispatch')
class OrderPayment(View):

    def post(self, request, order_id, amount):
        response = ZibalPaymentRequest(amount=amount)
        data = response.data
        track_id = data.get('track_id')

        if track_id:
            Payment.objects.create(
                order_id=order_id,
                amount=amount,
                track_id=track_id
            )

        return JsonResponse(data)


class OrderPaymentVerify(View):

    def get(self, request, *args, **kwargs):

        track_id = request.GET.get('trackId')
        success = request.GET.get('success')
        status = request.GET.get('status')

        response = ZibalPaymentVerification(track_id=track_id)
        data = response.data
        amount = data.get('amount')
        paid_at = data.get('paid_at')
        ref_number = data.get('refNumber')

        if not track_id or success != '1' or status != '2' or not amount:
            return JsonResponse(data)

        payment = get_object_or_404(Payment, track_id=track_id, amount=amount)

        payment.is_paid = True
        payment.paid_at = paid_at
        payment.ref_number = ref_number
        payment.save()
        send_message(
            medium='telegram',
            message='OK',
            receiver='09123456789'
        )

        return JsonResponse(data)
