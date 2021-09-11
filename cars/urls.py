from django.urls import path
from cars.views import car_detail, cars

urlpatterns = [
    path('', cars, name='cars'),
    path('car_detail/<int:pk>/', car_detail, name='car_detail'),
]
