from django.urls import path
from cars.views import car_detail, cars, search

urlpatterns = [
    path('', cars, name='cars'),
    path('car_detail/<int:pk>/', car_detail, name='car_detail'),
    path('search/', search, name='search'),
]
