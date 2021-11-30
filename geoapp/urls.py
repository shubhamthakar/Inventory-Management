from django.contrib import admin
from django.urls import path

import geoapp
from .views import *

urlpatterns = [

    path('', index, name='index'),
    path('accounts/login/', SignInView.as_view(), name="SignInView"),
    path('register/', RegistrationView.as_view(), name="RegistrationView"),
    path('signout/', SignOutView.as_view(), name="SignOutView"),
]
