from django.db import models
from django.contrib.gis.db import models

class Bank(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=5)
    poly = models.PolygonField()

    def __str__(self):
        return self.name
# Create your models here.
