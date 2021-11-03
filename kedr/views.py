from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import Http404
from rest_framework import routers, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import *
from .models import *
from .send_menejer import send_manager

# Create your views here.
from .serializers import ReviewSerializer, ReserveSerializer


def index(request):
    apartment_info = Apartment.objects.all()
    return render(request, 'kedr/index.html', context={'info': apartment_info})


def detail(request, slug):
    apartment_detail = get_object_or_404(Apartment, slug__iexact=slug)
    images = apartment_detail.photo_set.all()
    context = {
        'apartment_detail': apartment_detail,
        'images': images,

    }

    return render(request, 'kedr/detail.html', context)


class BookingApiView(APIView):
    def get(self, request):
        return Response({'message': 'success'}, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serialized_data = ReserveSerializer(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            send_manager(serialized_data.data)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.data, status=status.HTTP_400_BAD_REQUEST)


class Booking(View):
    def get(self, request):
        form = ReservationDate()
        return render(request, 'kedr/reserve.html', context={'form': form})


class CreateApart(LoginRequiredMixin, View):
    def get(self, request):
        form = ApartmentForm()
        formset = ApartmentFormSet()
        context = {'form': form, 'formset': formset}
        return render(request, 'kedr/create_apartment.html', context)

    def post(self, request):
        form = ApartmentForm(request.POST, request.FILES)
        if form.is_valid():
            bb = form.save()
            formset = ApartmentFormSet(request.POST, request.FILES, instance=bb)
            if formset.is_valid():
                formset.save()
                return redirect(index)
            else:
                context = {
                    'form': form, 'formset': formset
                }
                return render(request, 'kedr/create_apartment.html', context)


class UpdateApartment(LoginRequiredMixin, View):
    def get(self, request, slug):
        data = get_object_or_404(Apartment, slug=slug)
        form = ApartmentForm(instance=data)
        formset = ApartmentFormSet()
        context = {'form': form, 'formset': formset}
        return render(request, 'kedr/updete_apartment.html', context)

    def post(self, request, slug):
        data = get_object_or_404(Apartment, slug=slug)
        form = ApartmentForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save()
            formset = ApartmentFormSet(request.POST, request.FILES, instance=data)
            if formset.is_valid():
                formset.save()
                return redirect(index)
            else:
                context = {
                    'form': form, 'formset': formset
                }
                return render(request, 'kedr/create_apartment.html', context)


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


class ReviewView(APIView):

    def get(self, request):
        queryset = ApartmentReview.objects.all()
        serialized_data = ReviewSerializer()
        return Response(serialized_data.data)

    def post(self, request):
        data = request.data
        serialized_data = ReviewSerializer(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)


class ApartmentsReview(View):
    def get(self, request):
        form = ApartmentReviewForm()
        review = ApartmentReview.objects.all()
        context = {
            'form': form,
            'review': review
        }
        return render(request, 'kedr/review.html', context)


def other(request):
    return render(request, 'kedr/other.html')
