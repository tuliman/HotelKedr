from django.urls import path, include
from .views import *

urlpatterns = [
    path('', add_content, name='apartment_list_url'),
    path('booking/', Booking.as_view(), name='to_book_url'),
    path('add/apartment/', CreateApart.as_view(), name='create_apart_url'),
    path('kedr/<str:slug>/', detail, name='apartment_detail_url'),
    path('contact/', add_contact, name='contact_url'),
    path('one-room-apartment/', get_numbers, name='number_of_room'),
    path('two-room-apartment', get_number2, name='two_room_apartment'),
    path('three-room-apartment', get_number3, name='three_room_apartment'),

]
