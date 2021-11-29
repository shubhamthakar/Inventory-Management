from django.shortcuts import render, redirect

from django.shortcuts import render
from channels.layers import get_channel_layer
from django.core.serializers import serialize
from asgiref.sync import async_to_sync
from .models import *
# https://www.youtube.com/watch?v=r6oTcAYDRt0
# https://youtu.be/FKYZqAVyY8A
# Create your views here.
# def testPage(request):
#     return render(request, 'geoapp/index.html', {})

def index(request):
    channel_layer = get_channel_layer()
    data = Warehouse.objects.all()
    data = serialize('geojson', data, geometry_field='location')
    print(data)
    async_to_sync(channel_layer.group_send)(

        'mapConsumers' , {
            'type' : 'updateMap',
            'value' : data
            

        }
    )
    return render(request,'geoapp/index.html')
