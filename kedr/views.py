from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.generic import View
from .forms import *

from .models import *
from .send_menejer import send_manager


# Create your views here.

def add_content(request):
    apartment_info = Apartment.objects.all()
    return render(request, 'kedr/index.html', context={'info': apartment_info})


def detail(request, slug):
    apartment_detail = get_object_or_404(Apartment, slug__iexact=slug)

    return render(request, 'kedr/detail.html', context={'detail': apartment_detail})


class Booking(View):
    def get(self, request):
        form = ReservationDate()
        return render(request, 'kedr/reserve.html', context={'form': form})

    def post(self, request):
        bound_form = ReservationDate(request.POST)
        if bound_form.is_valid():
            new_reservation = bound_form.save()
            send_manager(bound_form.cleaned_data)

            return redirect('apartment_list_url')
        return render(request, 'kedr/reserve.html', context={'form': bound_form})


class CreateApart(View):
    def get(self, request):
        form = AddApartment()
        return render(request, 'kedr/create_apartment.html', context={'form': form})

    def post(self, request):
        bound_form = AddApartment(request.POST)
        if bound_form.is_valid():
            new_apart = bound_form.save()
            return redirect(new_apart)
        return render(request, 'kedr/create_apartment.html', context={'form': bound_form})


def get_numbers(request):
    room = Apartment.objects.filter(room_value='1')
    return render(request, 'kedr/number of room.html', context={'room': room})


def get_number2(request):
    room = Apartment.objects.filter(room_value='2')
    return render(request, 'kedr/number of room.html', context={'room': room})


def get_number3(request):
    room = Apartment.objects.filter(room_value='3')
    return render(request, 'kedr/number of room.html', context={'room': room})


def add_contact(request):
    return render(request, 'kedr/contacts.html')
