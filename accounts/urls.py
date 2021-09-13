from django.urls import path
from .views import login, signup, logout, dashboard

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),

]
