from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import Pdf


app_name = 'bookings'

urlpatterns = [
    path('',views.index, name='routes'),
    path('<int:pk>',views.make_a_booking, name='make_a_booking'),
    path('detail/<int:pk>',views.booking_detail, name='booking_detail'),
    path('ticket/<int:pk>',Pdf.as_view(),name='ticket'),
    path('search',views.search, name='search'), 
]

