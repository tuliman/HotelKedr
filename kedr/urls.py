from django.urls import path, include
from .views import index, Booking, BookingApiView, UpdateApartment, CreateApart, detail, DeleteApartment, add_contact, \
    get_numbers, get_number2, get_number3, ApartmentsReview, ReviewView

urlpatterns = [
    path('', index, name='apartment_list_url'),
    path('booking/', Booking.as_view(), name='to_book_url'),
    path('booking/api', BookingApiView.as_view()),
    path('detail/<str:slug>/update', UpdateApartment.as_view(), name='update_apartment'),
    path('add/apartment/', CreateApart.as_view(), name='create_apart_url'),
    path('detail/<str:slug>/', detail, name='apartment_detail_url'),
    path('detail/<str:slug>/delete', DeleteApartment.as_view(), name='delete_apartment'),
    path('contact/', add_contact, name='contact_url'),
    path('one-room-apartments/', get_numbers, name='number_of_room'),
    path('two-room-apartments/', get_number2, name='two_room_apartment'),
    path('three-room-apartments/', get_number3, name='three_room_apartment'),
    path('review/', ApartmentsReview.as_view(), name='apartment_review'),
    path('review/api', ReviewView.as_view())
]
