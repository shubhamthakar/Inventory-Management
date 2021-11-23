from django.contrib.gis import admin
from .models import *

admin.site.register(Shop)

admin.site.register(WorldBorder, admin.GeoModelAdmin)
# Register your models here.
