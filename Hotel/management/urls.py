from django.urls import path
from .views import ( bookHotel , showBookings , updateBookings , deleteBookings)

urlpatterns = [
    path('book/',bookHotel,name='book_hotel'),
    path('show/',showBookings,name='show_bookings'),
    path('update/<int:pk>/',updateBookings,name='update_bookings'),
    path('delete/<int:pk>/',deleteBookings,name='delete_bookings'),
]