import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django_daraja.mpesa.core import MpesaClient
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


# def index(request):
#     cl = MpesaClient()
#     token = cl.access_token()
#     print(token)
#     # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
#     phone_number = '0794721438'
#     amount = 1
#     account_reference = 'Msafiri Ticket'
#     transaction_desc = 'Description'
#     callback_url = request.build_absolute_uri(reverse('mpesa_stk_push_callback'))
#     response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
#     return HttpResponse(response.text)

@csrf_exempt
def stk_push_callback(request):
    data = request.body
    json_data = json.loads(data)
    print(json_data)
    # print(json_data['Value'])
    # You can do whatever you want with the notification received from MPESA here.
    return HttpResponse(data)