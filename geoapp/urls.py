from django.contrib import admin
from django.urls import path

import geoapp
from . import views

urlpatterns = [

    path('', views.index, name='index')
]