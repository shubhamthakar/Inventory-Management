from django.contrib.gis import admin
from .models import *

admin.site.register(Shop, admin.OSMGeoAdmin)

# admin.site.register(Shop)
admin.site.register(Warehouse, admin.GeoModelAdmin)
admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(BookedSlots, admin.GeoModelAdmin)
# Register your models here.
