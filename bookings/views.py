from threading import Thread, activeCount

import requests
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views.generic import View
from django_daraja.mpesa.core import MpesaClient

from accounts.models import CustomUser
from bookings.render import render_to_pdf
from buses.models import Bus
from mode_of_payments.models import ModeOfPayment
from payments.models import Payment
from travel_routes.choices import destinations
from travel_routes.models import TravelRoute

from .models import *
from .render import *

# Create your views here.


# send ticket to user after booking
def send_email(request):
    if request.user.is_authenticated:
        return requests.post(
            "https://api.mailgun.net/v3/sandbox5e710d75bee5465eb57b7ed5e34dd1c3.mailgun.org/messages",
            auth=("api", "9ceb1d896d45282e46374db17a6ddce1-65b08458-16ce32cc"),
            data={
                "from": "Msafiri Express <postmaster@sandbox5e710d75bee5465eb57b7ed5e34dd1c3.mailgun.org>",
                "to": [request.user.email],
                "subject": "Msafiri Express Ticket",
                "text": "Dear Customer, thank you for choosing Msafiri Express. Click on this link to download your ticket:",
            },
        )


class Pdf(View):
    def get(self, request, pk):
        if not request.user.is_authenticated:
            return HttpResponse("You are not allowed to view this resource.")
        template = get_template("ticket.html")
        booking = Booking.objects.get(pk=pk)
        route = TravelRoute()
        payment = Payment.objects.get(payment_for_id=booking.id)
        today = timezone.now()
        context = {
            "today": today,
            "booking": booking,
            "route": route,
            "payment": payment,
            "request": request,
        }
        html = template.render(context)
        pdf = render_to_pdf("ticket.html", context)

        if pdf:
            response = HttpResponse(pdf, content_type="application/pdf")
            filename = "%s" % ("Msafiri_Express_Ticket")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response["Content-Disposition"] = content
            send_email(request)
            return response
        return HttpResponse("Not found")


def index(request):
    routes = TravelRoute.objects.order_by("-publish_date").filter(is_published=True)

    paginator = Paginator(routes, 6)
    page = request.GET.get("page")
    paged_routes = paginator.get_page(page)

    context = {
        "routes": paged_routes,
    }
    return render(request, "bookings/routes.html", context)


def make_a_booking(request, pk):
    route = TravelRoute.objects.get(pk=pk)
    user = CustomUser()
    if not request.user.is_authenticated:
        messages.info(request, "Please login to proceed with booking.")
    elif request.method == "POST":
        form = request.POST
        # get form values
        booking = Booking()
        # get route price
        route = TravelRoute.objects.get(pk=pk)
        price = route.price
        booking.route = route
        booking.bus_details = Bus.objects.get(pk=form["bus_id"])
        booking.customer_details = CustomUser.objects.get(pk=form["user_id"])
        booking.number_of_tickets = request.POST["number_of_tickets"]
        booking.date_of_booking = request.POST["date_of_booking"]
        booking.amount_paid = int(booking.number_of_tickets) * int(price)

        cl = MpesaClient()
        token = cl.access_token
        print(token)
        # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
        phone_number = request.POST["mobile_number"]
        print(phone_number)
        amount = booking.amount_paid
        account_reference = "Msafiri Ticket"
        transaction_desc = "Description"
        callback_url = request.build_absolute_uri(reverse("mpesa_stk_push_callback"))
        print(callback_url)
        response = cl.stk_push(
            phone_number, amount, account_reference, transaction_desc, callback_url
        )
        # stay on payment page then redirect if successful
        # return HttpResponse(response.text)

        # payment
        payment = Payment()
        payment.customer_details = booking.customer_details
        payment.amount_paid = booking.amount_paid
        payment.mode_of_payment = ModeOfPayment.objects.get(pk=1)
        payment.payment_for = booking

        booking.save()
        payment.save()
        messages.success(request, "Booking successful.")
        return redirect("bookings:booking_detail", booking.pk)

    bookings = Booking.objects.all()
    context = {
        "route": route,
        "bookings": bookings,
    }
    return render(request, "bookings/booking.html", context)


def booking_detail(request, pk):
    booking = Booking.objects.get(pk=pk)
    route = TravelRoute()
    payment = Payment.objects.get(payment_for_id=booking.id)

    context = {
        "booking": booking,
        "route": route,
        "payment": payment,
    }
    return render(request, "bookings/booking_detail.html", context)


def search(request):
    queryset_list = TravelRoute.objects.order_by("-date_of_travel").filter(
        is_published=True
    )

    # Origin
    if "origin" in request.GET:
        origin = request.GET["origin"]
        if origin:
            queryset_list = queryset_list.filter(origin__iexact=origin)

    # Destination
    if "destination" in request.GET:
        destination = request.GET["destination"]
        if destination:
            queryset_list = queryset_list.filter(destination__iexact=destination)

    # Date of Travel
    if "date_of_travel" in request.GET:
        date_of_travel = request.GET["date_of_travel"]
        if date_of_travel:
            queryset_list = queryset_list.filter(date_of_travel__iexact=date_of_travel)

    context = {
        "destinations": destinations,
        "routes": queryset_list,
        "values": request.GET,
    }
    return render(request, "bookings/search.html", context)
