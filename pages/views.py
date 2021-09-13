from django.shortcuts import render
from .models import Team
from cars.models import Car


def home(request):
    team = Team.objects.all()
    featured_cars = Car.objects.filter(is_featured=True, for_rent=True)
    last_cars = Car.objects.filter(for_sale=True)
    context = {
        'teams': team,
        'featured_cars': featured_cars,
        'last_cars': last_cars
    }
    return render(request, 'pages/index.html', context=context)


# Create your views here.
def cars(request):
    return render(request, 'pages/cars.html')


def about(request):
    team = Team.objects.all()
    context = {
        'teams': team
    }
    return render(request, 'pages/about.html', context=context)


def contact(request):
    return render(request, 'pages/contact.html')


def service(request):
    return render(request, 'pages/service.html')


def login(request):
    return render(request, 'pages/login.html')


def login_up(request):
    return render(request, 'pages/sigup.html')
