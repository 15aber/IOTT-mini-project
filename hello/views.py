from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.views.generic import View
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import Greeting, Mdata
from .serializers import API_dataSerializer


class HomeView(View):
    def get(self, request, *args, **kwargs):
        data = Mdata.objects.last()
        return render(request, 'home.html', {"data": data})

class TempView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'temp.html', {})

class BatteryView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'battery.html', {})
        
class PresView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pres.html', {})

class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html', {})

class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html', {})

# Create your views here.
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')
    
    # return HttpResponse('Hello from Python!')
    # return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

class API(generics.ListAPIView):
    queryset = Mdata.objects.all()
    serializer_class = API_dataSerializer



class ChartData(APIView):
        authentication_classes = []
        permission_classes = []

        def get(self, request, format = None):
            battery = []
            temp = []
            time = []
            pres = []
            for i in Mdata.objects.all():
                battery.append(i.battery)
                temp.append(i.temp)
                time.append(i.published_at)
                pres.append(i.pressure)
            
            data = { 
                "time": time, 
                "battery": battery,
                "temp": temp,
                "pres": pres
            }
            return Response(data)


#@require_POST
@csrf_exempt
def handle_particle_hook(request):
    #jsondata = {"event":"temp","data":"{\"b\":\"88.36\",\"t\":\"24.10\",\"p\":\"1000\"}","published_at":"2018-11-12T08:06:00.343Z","coreid":"2b004f001351363038393739","userid":"5bd2ce8157165964b576aefc","fw_version":1,"public":"false"}
    jsondata = json.loads(request.body)
    data1 = jsondata['data']
    data2 = json.loads(data1)
    mdata = Mdata()
    mdata.device_id = jsondata['coreid']
    mdata.battery = float(data2['b'])
    mdata.temp = float(data2['t'])
    mdata.pressure = data2['p']
    mdata.save()
    return HttpResponse(200)