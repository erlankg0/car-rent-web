from django.shortcuts import render


def cars(request):
    return render(request, 'pages/cars.html')
# Create your views here.
