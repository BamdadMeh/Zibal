import json
import requests
from django.urls import reverse


def send_message(medium, message, receiver):

    req_header = {
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    host = 'http://localhost:8000'
    path = reverse('medium:medium', kwargs={'medium': medium})
    url = f'{host}{path}'

    requests.post(
        url=url,
        data=json.dumps({'message': message, 'receiver': receiver}),
        headers=req_header
    )
