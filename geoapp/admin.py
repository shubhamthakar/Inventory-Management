from django.contrib.gis import admin
from .models import *



# admin.site.register(Shop)
admin.site.register(Warehouse, admin.OSMGeoAdmin)
admin.site.register(BookedSlots, admin.OSMGeoAdmin)
# Register your models here.
