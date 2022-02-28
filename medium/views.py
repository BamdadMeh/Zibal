from django.http import JsonResponse
from django.views import View
import json
from medium.send_message import send_message
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class SendMessage(View):

    def post(self, request, medium, *args, **kwargs):

        try:
            info = json.loads(request.body)
            send_message.delay(medium=medium, info=info)

        except:
            return JsonResponse({'error': 'data is invalid'})

        data = {
            'status': 'Sent',
            'medium': medium,
            'info': info,
        }
        return JsonResponse(data)
