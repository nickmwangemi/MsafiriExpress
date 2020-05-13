from django.shortcuts import render
from travel_routes.models import TravelRoute
from travel_routes.choices import destinations


# Create your views here.
def index(request):
    routes = TravelRoute.objects.order_by('-publish_date').filter(is_published=True)[:3]

    context = {
        'destinations':destinations,
        'routes':routes,
    }

    return render(request, 'pages/index.html',context)

def about(request):
    return render(request, 'pages/about.html')