from django.contrib import admin

from .models import TravelRoute


# Register your models here.
class TravelRouteAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "origin",
        "destination",
        "date_of_travel",
        "time_of_departure",
        "bus_type",
        "publish_date",
        "is_published",
        "price",
    )
    list_editable = ["time_of_departure", "is_published", "price"]


admin.site.register(TravelRoute, TravelRouteAdmin)
