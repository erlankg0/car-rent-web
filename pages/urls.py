from django.urls import path
from .views import home, about, contact, service, login_up, login

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('service/', service, name='service'),
    path('login/', login, name='login'),
    path('login_up/', login_up, name='login_up'),
]
