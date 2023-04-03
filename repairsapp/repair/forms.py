from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from .models import *
import json

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