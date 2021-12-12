from django.contrib import admin

from .models import CustomUser


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "mobile_number", "is_staff", "is_active"]
    list_editable = ["email", "mobile_number", "is_staff", "is_active"]


admin.site.register(CustomUser, CustomUserAdmin)
