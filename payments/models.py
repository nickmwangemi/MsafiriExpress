from django.db import models

from accounts.models import CustomUser
from bookings.models import Booking
from mode_of_payments.models import ModeOfPayment
from travel_routes.models import TravelRoute


# Create your models here.
class Payment(models.Model):
    customer_details = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount_paid = models.FloatField()
    mode_of_payment = models.ForeignKey(ModeOfPayment, on_delete=models.CASCADE)
    payment_for = models.ForeignKey(Booking, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return str(self.amount_paid)

    class Meta:
        db_table = "tbl_Payments"
