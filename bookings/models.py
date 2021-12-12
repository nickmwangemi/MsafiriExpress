from django.contrib.auth.models import User
from django.db import models

from accounts.models import CustomUser
from buses.models import Bus
from travel_routes.models import TravelRoute

# Create your models here.


class Booking(models.Model):
    route = models.ForeignKey(TravelRoute, on_delete=models.CASCADE)
    bus_details = models.ForeignKey(Bus, on_delete=models.CASCADE)
    customer_details = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    number_of_tickets = models.IntegerField(default=1)
    date_of_booking = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return str(self.route)

    class Meta:
        verbose_name_plural = "Bookings"
        db_table = "tbl_Bookings"
