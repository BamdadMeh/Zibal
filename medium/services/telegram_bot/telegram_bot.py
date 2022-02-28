from medium.services.base import _Medium
import requests
import json


class TelegramBot(_Medium):

    url = 'https://interview-bot.zibal.ir/notify'

    def send(self, message, receiver):

        req_header = {
            'Content-Type': 'application/json'
        }
        req_data = {
            'token': 'U2FsdGVkX19lbW9LLYKBz/wHmnJ6RPhCP0WtGYmtHYM=',
            'message': 'Hello World',

        }

        response = requests.post(
            url=TelegramBot.url,
            data=json.dumps(req_data),
            headers=req_header
        )

        return response


__all__ = (

    'TelegramBot',
)
