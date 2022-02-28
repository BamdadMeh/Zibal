from abc import ABC
from decouple import config
from django.urls import reverse
import requests
import json


class _Zibal(ABC):

    _MERCHANT = config('ZIBAL_MERCHANT')
    _API_REQUEST = 'https://gateway.zibal.ir/v1/request'
    _API_VERIFY = 'https://gateway.zibal.ir/v1/verify'
    _API_STARTPAY = 'https://gateway.zibal.ir/start/'

    req_header = {
            'accept': 'application/json',
            'content-type': 'application/json'
    }


class ZibalPaymentRequest(_Zibal):

    def __init__(self, amount, *args, **kwargs):

        host = 'http://localhost:8000'
        path = reverse('payment:order_payment_verify')
        callback_url = f'{host}{path}'

        req_data = {
            'merchant': _Zibal._MERCHANT,
            'amount': amount,
            'callbackUrl': callback_url,
        }

        req = requests.post(
            url=_Zibal._API_REQUEST,
            data=json.dumps(req_data),
            headers=_Zibal.req_header
        )

        response = req.json()

        result = response.get('result')
        track_id = response.get('trackId')
        message = response.get('message')

        self.data = {'message': message}

        if result == 100 and track_id:
            self.data['track_id'] = track_id
            self.data['payment_gateway'] = f'{_Zibal._API_STARTPAY}{track_id}'


class ZibalPaymentVerification(_Zibal):

    def __init__(self, track_id):

        req_data = {
            'merchant': _Zibal._MERCHANT,
            'trackId': track_id
        }

        req = requests.post(
            url=_Zibal._API_VERIFY,
            data=json.dumps(req_data),
            headers=_Zibal.req_header
        )

        response = req.json()

        result = response.get('result')
        status = response.get('status',)
        message = response.get('message', 'An error has occurred')
        ref_number = response.get('refNumber')
        paid_at = response.get('paidAt')
        amount = response.get('amount')

        self.data = {
            'message': message,
            'paid': False
        }

        if result == 100 and status == 1:

            self.data['ref_number'] = ref_number
            self.data['paid_at'] = paid_at
            self.data['amount'] = amount
            self.data['paid'] = True
        elif result == 201:
            self.data['paid'] = True


__all__ = (

    'ZibalPaymentRequest',
    'ZibalPaymentVerification',
)
