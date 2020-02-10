from django.forms import formset_factory, ModelForm, TextInput, EmailInput, NumberInput, Textarea, modelform_factory
from .models import *
from django.core.exceptions import ValidationError


class ReservationDate(ModelForm):
    class Meta:
        model = ToBook
        fields = ['name', 'email', 'phone_number', 'description']
        labels = {
            'name': 'Имя',
            'phone_number': 'Телефонный номер',
            "description": 'Пожелания по подбору'
        }
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'phone_number': NumberInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
        }


class AddApartment(ModelForm):
    class Meta:
        model = Apartment

        fields = '__all__'

        labels = {
            'name': 'Название квартиры',
            'slug': 'Уникальный индефикатор',
            'description_title': 'Краткое описание',
            'description': 'Полное описание',
            'price': 'Цена аренды',
            'room_value': 'Количество комнат'
        }
