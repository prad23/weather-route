from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from .models import Network


def index(request):
    device_list = Network.objects.order_by('-pub_date')
      #  output = ",".join([d.device_text for d in device_list])
    context = {'device_list':device_list}
    return render(request,'currentLocation/index.html',context)

def detail(request,device_id):
    try:
        device = Network.objects.get(pk=device_id)
    except Network.DoesNotExist:
        raise Http404("Device id %s does not exist." %device_id)
    return render(request,'currentLocation/detail.html',{'device':device})