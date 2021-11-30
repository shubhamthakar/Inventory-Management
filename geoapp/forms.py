from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .models import *
from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User

class SignInForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            'password' : forms.PasswordInput(attrs={'class': 'input'}),
            'username': forms.TextInput(attrs={'class': 'input'}),
            }

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "email"]
        widgets = {
            'password' : forms.PasswordInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            }