from django.shortcuts import render, get_object_or_404
from cars.models import Car
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger


def cars(request):
    all_cars = Car.objects.all()
    paginator = Paginator(all_cars, 6)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    context = {
        'all_cars': paged_cars,
    }
    return render(request, 'pages/cars.html', context=context)


# Create your views here.

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    context = {
        'car': car
    }

    return render(request, 'cars/car_detail.html', context=context)


def search(request):
    search_cars = Car.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            search_cars = search_cars.filter(car_title__icontains=keyword)
    context = {
        'search_cars': search_cars
    }
    return render(request, 'cars/search.html', context=context)
