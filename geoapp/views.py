from django.shortcuts import render, redirect
from channels.layers import get_channel_layer
from django.core.serializers import serialize
from asgiref.sync import async_to_sync
from .models import *
from django.views import View
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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



class SignInView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('index')
        form = SignInForm()
        return render(request, 'geoapp/signin.html', {"form":form})

    def post(self,request):
        if request.user.is_authenticated:
            return redirect('index')

        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return redirect('SignInView')

class RegistrationView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('index')
        form = RegisterForm()
        return render(request, 'geoapp/registration.html', {"form":form})

    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = User.objects.create_user(username=username,email= email,password=password)
            user.save()
            messages.success(request, 'Account was created for ' + username)
            return redirect('SignInView')
        else:
            messages.info(request, 'Input correct details')
        return render(request, 'geoapp/registration.html', {"form":form})
        

class SignOutView(View):
    
    def get(self,request):
        logout(request)
        return redirect('SignInView')
