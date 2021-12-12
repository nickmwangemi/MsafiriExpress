from django.contrib import admin

from .models import ModeOfPayment


# Register your models here.
class ModeOfPaymentAdmin(admin.ModelAdmin):
    list_display = ["mode_of_payment"]


admin.site.register(ModeOfPayment, ModeOfPaymentAdmin)
