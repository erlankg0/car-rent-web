from django.shortcuts import render, get_object_or_404
from cars.models import Car


def cars(request):
    return render(request, 'pages/cars.html')


# Create your views here.

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    context = {
        'car': car
    }
    return render(request, 'cars/car_detail.html', context=context)
