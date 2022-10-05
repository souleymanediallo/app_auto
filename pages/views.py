from django.shortcuts import render
from .models import Team
from cars.models import Car


# Create your views here.
def home(request):
    cars_featured = Car.objects.all()
    cars_latest = Car.objects.order_by('-created_date')
    context = {'cars_featured': cars_featured, 'cars_latest': cars_latest}
    return render(request, "pages/index.html", context)


def about(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, "pages/about.html", context)


def services(request):
    return render(request, "pages/services.html")


def contact(request):
    return render(request, "pages/contact.html")