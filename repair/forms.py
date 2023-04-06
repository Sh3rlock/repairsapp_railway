from pickle import TRUE
from django import forms
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django.forms import widgets
from .models import *
import json

class DateInput(forms.DateInput):
    input_type = 'date'


class UserLoginForm(forms.ModelForm):
    username = forms.CharField(
                            widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),
                            required=True)
    password = forms.CharField(
                            widget=forms.PasswordInput(attrs={'id': 'floatingPassword', 'class': 'form-control mb-3'}),
                            required=True)

    class Meta:
        model=User
        fields=['username','password']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['clientName', 'phoneNumber', 'emailAddress', 'note']
        labels = {
            'clientName': 'Név:',
            'phoneNumber': 'Telefon:',
            'emailAddress': 'Email:',
            'note': 'Megjegyzés:',
        }