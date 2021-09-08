from django.shortcuts import render


def home(request):
    return render(request, 'pages/index.html')


# Create your views here.
def cars(request):
    return render(request, 'pages/cars.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def service(request):
    return render(request, 'pages/service.html')
