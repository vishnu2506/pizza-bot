from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from bot.models import Order
from django.utils import timezone
import datetime
from datetime import timedelta
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import json

# Create your views here.

def land(request):
    return render(request, 'bot/base.html')

@csrf_exempt
def saveOrder(request):
    if request.method == 'post' or request.method == 'POST':
        print(request.body)
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        newOrder = Order(
            pizzaType = data['pizzaType'],
            pizzaName = data['pizzaName'],
            pizzaSize = data['pizzaSize'],
            baseType = data['baseType'],
            toppings = (str(data['toppings']) if 'toppings' in data else ''),
            contactName = data['name'],
            contactNumber = int(data['phone'],),
            address = data['address'],
            orderDate = str(datetime.datetime.now()),
        )
        newOrder.save()
        respone = {
            'success': True,
            'orderId': newOrder.pk,
            'requestData': request.GET
        }
        return JsonResponse(respone)
    else:
        respone = {
            'success': False,
            'message': 'Sorry I could not process your request!'
        }

@csrf_exempt
def checkStatus(request):
    if request.method == 'post' or request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        orderDetail = get_object_or_404(Order, pk = data['orderId'])    
        datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
        diff = datetime.datetime.strptime(str(datetime.datetime.now()), datetimeFormat)\
                - datetime.datetime.strptime(orderDetail.orderDate, datetimeFormat)
        if diff.seconds/60 < 15.00:
            return JsonResponse({'message': 'Pizza is in the kitchen yet'})
        elif diff.seconds/60 >= 15.00 and diff.seconds/60 < 30.00:
            return JsonResponse({'message': 'Your pizza is on the way!'})
        elif diff.seconds/60 >= 30.00:
            orderDetail.status = 'Delievered'
            orderDetail.save()
            return JsonResponse({'message': 'You have recieved your pizza!'})
        
        return JsonResponse({'message': 'sorry could not found your order :('})