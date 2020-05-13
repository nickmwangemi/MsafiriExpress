from django.contrib import admin
from .models import Bus

# Register your models here.
class BusAdmin(admin.ModelAdmin):
    list_display = ('type','reg_number','number_of_seats')

admin.site.register(Bus,BusAdmin)