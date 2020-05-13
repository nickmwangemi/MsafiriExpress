from django.contrib import admin
from .models import Booking

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ('route','bus_details', 'customer_details','number_of_tickets','date_of_booking')
    list_per_page = 10


admin.site.register(Booking,BookingAdmin)
