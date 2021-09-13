from django.shortcuts import render, get_object_or_404
from cars.models import Car
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger


def cars(request):
    all_cars = Car.objects.all()
    paginator = Paginator(all_cars, 6)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    search_model = Car.objects.values_list('model', flat=True).distinct()
    search_city = Car.objects.values_list('city', flat=True).distinct()
    search_year = Car.objects.values_list('year', flat=True).distinct()
    search_fuel_type = Car.objects.values_list('fuel_type', flat=True).distinct()
    search_transmission = Car.objects.values_list('transmission', flat=True).distinct()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            all_cars = all_cars.filter(car_title__icontains=keyword)

    if 'select-brand' in request.GET:
        brand = request.GET['select-brand']
        if brand:
            all_cars = all_cars.filter(model__icontains=brand)

    if 'select-location' in request.GET:
        city = request.GET['select-location']
        if city:
            all_cars = all_cars.filter(city__icontains=city)
    if 'select-year' in request.GET:
        year = request.GET['select-year']
        if year:
            all_cars = all_cars.filter(year__icontains=year)

    if 'select-type' in request.GET:
        body = request.GET['select-type']
        if body:
            all_cars = all_cars.filter(body_style__icontains=body)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            all_cars = all_cars.filter(price_for_sale__gte=min_price, price_for_sale__lte=max_price)

    if 'select-fuel_type' in request.GET:
        fuel_type = request.GET['select-fuel_type']
        if fuel_type:
            all_cars = all_cars.filter(fuel_type__icontains=fuel_type)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            all_cars = all_cars.filter(transmission__icontains=transmission)
    context = {
        'search_cars': all_cars,
        'search_model': search_model,
        'search_city': search_city,
        'search_year': search_year,
        'search_fuel_type': search_fuel_type,
        'search_transmission': search_transmission,
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
    search_model = Car.objects.values_list('model', flat=True).distinct()
    search_city = Car.objects.values_list('city', flat=True).distinct()
    search_year = Car.objects.values_list('year', flat=True).distinct()
    search_fuel_type = Car.objects.values_list('fuel_type', flat=True).distinct()
    search_transmission = Car.objects.values_list('transmission', flat=True).distinct()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            search_cars = search_cars.filter(car_title__icontains=keyword)

    if 'select-brand' in request.GET:
        brand = request.GET['select-brand']
        if brand:
            search_cars = search_cars.filter(model__icontains=brand)

    if 'select-location' in request.GET:
        city = request.GET['select-location']
        if city:
            search_cars = search_cars.filter(city__icontains=city)
    if 'select-year' in request.GET:
        year = request.GET['select-year']
        if year:
            search_cars = search_cars.filter(year__icontains=year)

    if 'select-type' in request.GET:
        body = request.GET['select-type']
        if body:
            search_cars = search_cars.filter(body_style__icontains=body)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            search_cars = search_cars.filter(price_for_sale__gte=min_price, price_for_sale__lte=max_price)

    if 'select-fuel_type' in request.GET:
        fuel_type = request.GET['select-fuel_type']
        if fuel_type:
            search_cars = search_cars.filter(fuel_type__icontains=fuel_type)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            search_cars = search_cars.filter(transmission__icontains=transmission)
    context = {
        'search_cars': search_cars,
        'search_model': search_model,
        'search_city': search_city,
        'search_year': search_year,
        'search_fuel_type': search_fuel_type,
        'search_transmission': search_transmission,
    }
    return render(request, 'cars/search.html', context=context)
