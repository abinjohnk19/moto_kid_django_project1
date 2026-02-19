from django.contrib import admin
from .models import Departments,Mechanic,Booking
from .views import booking

# Register your models here.


admin.site.register(Departments)
admin.site.register(Mechanic)

class BookingAdmin(admin.ModelAdmin):
    list_display=('id','c_name','c_phone','c_email','dep_name','booking_date','booked_on')
admin.site.register(Booking,BookingAdmin)
