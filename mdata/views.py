from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

from .models import Mdata

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mdata/charts.html', {})

def index(request):
    mdata = Mdata.objects.all()[:10]

    context = {
    'title': 'Hello from index!!!',
    'mdata': mdata
}

    return render(request, 'mdata/charts.html', context)

def get_data(request, *args, **kwargs):
    data = { "sales":100, "customer":10 }
    return JsonResponse(data)

class ChartData(APIView):
        authentication_classes = []
        permission_classes = []
        
        def get(self, request, format = None):
            labels = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"]
            default_items = [10, 20, 60, 1, 5, 35]
            data = { 
                 "labels": labels, 
                 "default": default_items,
            }
            return Response(data)


@csrf_exempt
def webhook_receiver(request):
    return HttpResponse(200)