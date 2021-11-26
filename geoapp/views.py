from django.shortcuts import render
from channels.layers import get_channel_layer
from django.core.serializers import serialize
from asgiref.sync import async_to_sync
from .models import *
# Create your views here.

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
    return render(request,'index.html')