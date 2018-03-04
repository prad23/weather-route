from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Network
from django.template import loader

'''def index(request):
    return HttpResponse("Hello, Welcome to current location.")

def device(request,devicename):
    return HttpResponse("Results for Device: %s" %devicename)
'''
def index(request):
    device_list = Network.object.order_by('-pub_date')[:5]
  #  output = ",".join([d.device_text for d in device_list])
    template = loader.get_template('currentLocation/index.html')
    context = {
        'device_list':device_list,
    }
    return HttpResponse(template.render(context,request))