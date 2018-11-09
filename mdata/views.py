from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

from .models import Mdata

# Create your views here.


def index(request):
    mdata = Mdata.objects.all()[:10]

    context = {
    'title': 'Hello from index!!!',
    'mdata': mdata
}

    return render(request, 'mdata/index.html', context)

def get_data(request, *args, **kwargs):
    data = { "sales":100, "customer":10 }
    return JsonResponse(data)

@csrf_exempt
def webhook_receiver(request):
    return HttpResponse(200)