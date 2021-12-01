from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.serializers import serialize
from geoapp.models import BookedSlots, Warehouse
import uuid
from django.contrib.auth.models import User

class TableData(AsyncWebsocketConsumer):

    async def connect(self):
        self.group_name='mapConsumers'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self,close_code):
        pass

    async def receive(self,text_data):
        print(text_data)
        arr = list(text_data.split())
        id, noOfSlots, username = arr[0], int(arr[1]), arr[2]
        print(id)
        print(noOfSlots)
        print("----",self.scope["user"],"----")
        id = uuid.UUID(id)
        
        warehouse = Warehouse.objects.get(warehouseId=id)
        if (warehouse.availableSlots >= noOfSlots):
            warehouse.availableSlots -= noOfSlots
            #user = User.objects.get(username=self.scope["user"])
            user = User.objects.get(username=username)
            BookedSlots.objects.create(warehouse=warehouse, user=user, bookingFees=warehouse.bookingFees, noOfSlots=noOfSlots)
            warehouse.save()
            data = Warehouse.objects.all()
            warehouse_details = serialize('geojson', data, geometry_field='location')
        else:
            warehouse_details = {"Error": "No slots available"}


        await self.channel_layer.group_send(
            self.group_name,
            {
                'type':'updateMap',
                'value':warehouse_details,
            }
        )

    async def updateMap(self,event):
        print (event['value'])
        await self.send(event['value'])
