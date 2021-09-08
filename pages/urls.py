from django.urls import path
from .views import home, about, contact, service, cars

urlpatterns = [
    path('', home, name='home'),
    path('carhouse/about/', about, name='about'),
    path('carhouse/contact/', contact, name='contact'),
    path('carhouse/cars/', cars, name='cars'),
    path('carhouse/service/', service, name='service'),
]
