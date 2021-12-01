from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.admin import OSMGeoAdmin
import uuid
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class Warehouse(models.Model):
    warehouseId = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    availableSlots = models.IntegerField()
    bookingFees = models.DecimalField(max_digits=10, decimal_places=2)        

    def __str__(self):
        return self.name


class BookedSlots(models.Model):
    bookingId = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    warehouse = models.ForeignKey(Warehouse, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)
    bookingFees = models.DecimalField(max_digits=10, decimal_places=2)
    timestampOfBooking = models.TimeField(auto_now_add=True)
    isPaid = models.BooleanField(default=False)
    noOfSlots = models.IntegerField()

    def __str__(self):
        return str(self.bookingId)


