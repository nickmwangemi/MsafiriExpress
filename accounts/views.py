from django.shortcuts import render, redirect
from django.contrib import messages, auth
from accounts.models import CustomUser
from .models import CustomUser
from django.contrib.auth import authenticate
from bookings.models import Booking
from payments.models import Payment
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from travel_routes.models import TravelRoute




# Create your views here.
def register(request):
   if request.method != 'POST':
      return render(request, 'accounts/register.html')
   # Get form values
   full_name = request.POST['full_name']
   email = request.POST['email']
   mobile_number = request.POST['mobile_number']
   password = request.POST['password']
   password2 = request.POST['password2']

   if password == password2:
      if CustomUser.objects.filter(mobile_number=mobile_number).exists():
         messages.error(request, 'That mobile number is already in use')
         return redirect('accounts:register')
      else:
         if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'That email is already taken')
            return redirect('accounts:register')
         else:
            # Looks good
            user = CustomUser()
            user.full_name = full_name
            user.email = email
            user.mobile_number = mobile_number
            user.password = password

            user = CustomUser.objects.create_user(full_name=full_name,email=email,mobile_number=mobile_number, password=password)
            user.save()

            # Login after register
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('accounts:dashboard')
   else:
      messages.error(request, 'Passwords do not match')
      return redirect('accounts:register')


def registermodal(request,pk):
   route = TravelRoute.objects.get(pk=pk)
   if request.method == 'POST':
      full_name = request.POST['full_name']
      email = request.POST['email']
      mobile_number = request.POST['mobile_number']
      password = request.POST['password']
      password2 = request.POST['password2']

      if password == password2:
         if CustomUser.objects.filter(mobile_number=mobile_number).exists():
            messages.error(request, 'That mobile number is already in use')
            route = TravelRoute.objects.get(pk=pk)
            return redirect('accounts:registermodal',route.pk)
         else:
            if CustomUser.objects.filter(email=email).exists():
               messages.error(request, 'That email is already taken')
               route = TravelRoute.objects.get(pk=pk)
               return redirect('accounts:registermodal',route.pk)
            else:
            # Looks good
               user = CustomUser()
               user.full_name = full_name
               user.email = email
               user.mobile_number = mobile_number
               user.password = password
               
               user = CustomUser.objects.create_user(full_name=full_name,email=email,mobile_number=mobile_number, password=password)
               user.save()

               # Login after register
               auth.login(request, user)
               messages.success(request, 'You are now logged in')
               
               route = TravelRoute.objects.get(pk=pk)
               return redirect('bookings:make_a_booking',route.pk)
      else:
         messages.error(request, 'Passwords do not match')
         route = TravelRoute.objects.get(pk=pk)
         return redirect('accounts:registermodal',route.pk)
   else:
      route = TravelRoute.objects.get(pk=pk)
      context = {
         'route':route,
      }
      return render(request, 'bookings/booking.html',context)


def login(request):
   if request.method != 'POST':
      return render(request, 'accounts/login.html')
   email = request.POST['email']
   password = request.POST['password']

   user = authenticate(email=email, password=password)

   if user is not None:
      auth.login(request,user)
      messages.success(request, 'You are now logged in')
      return redirect('accounts:dashboard')
   else:
      messages.error(request, 'Invalid credentials')
      return redirect('accounts:login')


def loginmodal(request,pk):
   if request.method == 'POST':
      email = request.POST['email']
      password = request.POST['password']
      
      user = authenticate(email=email, password=password)
      
      if user is not None:
         auth.login(request,user)
         messages.success(request, 'You are now logged in')
         route = TravelRoute.objects.get(pk=pk)
         return redirect('bookings:make_a_booking',route.pk)
      else:
         messages.error(request, 'Invalid credentials')
         route = TravelRoute.objects.get(pk=pk)
         return redirect('accounts:loginmodal',route.pk)
   else:
      route = TravelRoute.objects.get(pk=pk)
      context = {
         'route':route,
      }
      
      return render(request, 'bookings/booking.html',context)


def logout(request):
   if request.method == 'POST':
      auth.logout(request)
      messages.success(request, 'You are now logged out')
      return redirect('pages:index')


def dashboard(request):
   user = CustomUser()
   if not request.user.is_authenticated:
      messages.info(request,'Please login to proceed.')
      return redirect('accounts:login')
   else:
      customer_id = request.user.id
      bookings = Booking.objects.order_by('-date_of_booking').filter(customer_details_id=customer_id)
      payment = Payment.objects.filter(customer_details_id=customer_id)

      paginator = Paginator(bookings,5)
      page = request.GET.get('page')
      paged_bookings = paginator.get_page(page)

      context = {
         'bookings':paged_bookings,
         'payment':payment,
      }

      return render(request, 'accounts/dashboard.html',context)


