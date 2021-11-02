from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='apartment_list_url'),
    path('booking/', Booking.as_view(), name='to_book_url'),
    path('other/',other,name = 'other'),
    path('detail/<str:slug>/update', UpdateApartment.as_view(), name='update_apartment'),
    path('add/apartment/', CreateApart.as_view(), name='create_apart_url'),
    path('detail/<str:slug>/', detail, name='apartment_detail_url'),
    path('contact/', add_contact, name='contact_url'),
    path('one-room-apartments/', get_numbers, name='number_of_room'),
    path('two-room-apartments/', get_number2, name='two_room_apartment'),
    path('three-room-apartments/', get_number3, name='three_room_apartment'),
    path('review/', ApartmentsReview.as_view(), name='apartment_review'),
    path('review/api', ReviewView.as_view())
]
