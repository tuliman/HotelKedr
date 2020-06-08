from django import forms
from django.forms import inlineformset_factory
from .models import *
from django.core.exceptions import ValidationError


class ReservationDate(forms.ModelForm):
    class Meta:
        model = ToBook
        fields = ['name', 'email', 'phone_number', 'description']
        labels = {
            'name': 'Имя',
            'phone_number': 'Телефонный номер',
            "description": 'Пожелания по подбору'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'


ApartmentFormSet = inlineformset_factory(Apartment, Photo, fields='__all__')
