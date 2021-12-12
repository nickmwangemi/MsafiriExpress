from django.contrib import admin

from .models import Payment


# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "customer_details",
        "amount_paid",
        "payment_for",
        "mode_of_payment",
        "timestamp",
    )


admin.site.register(Payment, PaymentAdmin)
