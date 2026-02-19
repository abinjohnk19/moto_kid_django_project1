from django import forms
from .models import  Booking

class DateInput(forms.DateInput):
     input_type ='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model= Booking
        fields='__all__'

        widgets={
            'booking_date':DateInput(),

        }

        labels ={
            'c_name': "Name:",
            'c_phone' :"Phone:",
            'c_email' :"Email:",
            'dep_name' : "Department",
            'booking_date' :"Booking Date",
        }