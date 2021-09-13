from django.shortcuts import render, redirect


def login(request):
    return render(request, 'accounts/login.html')


def signup(request):
   if request.method == 'POST':

    return render(request, 'accounts/signup.html')


def logout(request):
    return redirect('home')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
