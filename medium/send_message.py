from medium.models import MediumReport
from medium.services import *
from celery import shared_task


MEDIUMS = {
    'telegram': TelegramBot,
    'mail': Mail,
    'sms': SMS,
    'push_notification': PushNotification,
    'user_inbox': UserInbox,
}


@shared_task
def send_message(medium, info, *args, **kwargs):

    message = info.get('message')
    receiver = info.get('receiver')

    if medium in MEDIUMS and message and receiver:
        sender = MEDIUMS[medium]()

        response = sender.send(
            message=info['message'],
            receiver=info['receiver']
        )

        # Here we can implement exactlye once !

        MediumReport.objects.create(
            message=info['message'],
            medium=medium,
            receiver=info['receiver']
        )
