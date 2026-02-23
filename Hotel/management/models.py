from django.db import models

# Create your models here.
from django.db import models

class HotelRoom(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_address = models.TextField()
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    room_price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.CharField(max_length=20, default="Available")
    date_added = models.DateTimeField(auto_now_add=True)   # automatically set when created
    date_updated = models.DateTimeField(auto_now=True)     # automatically set when modified