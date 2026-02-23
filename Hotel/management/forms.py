from django import forms
from .models import HotelRoom

ROOM_TYPES = [
        ("Single", "Single"),
        ("Double", "Double"),
        ("Suite", "Suite"),
        ("Deluxe", "Deluxe"),
    ]


class HotelRoomForm(forms.ModelForm):
    class Meta:
        model = HotelRoom
        fields = '__all__'
        labels = {
            'hotel_name':'Hotel Name',
            'hotel_address':'Hotel Address',
            'room_number':'Room No',
            'room_type':'Room Type',
            'room_price':'Room Price',
            'availability':'Availability'
        }
        widgets = {
            'hotel_name':forms.TextInput(attrs={
                'placeholder':'Enter Hotel Name'
            }),
            'hotel_address':forms.Textarea(attrs={
                'rows':'3'
            }),
            'room_number':forms.TextInput(attrs={
                'placeholder':'E.g., 101'
            }),
            'room_type':forms.Select(choices=ROOM_TYPES)
        }