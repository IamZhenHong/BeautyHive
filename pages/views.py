from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def landing(request):
    return render(request, 'pages/landing.html')

@login_required
def customer_home(request):
    return render(request, 'pages/customer_home.html')

@login_required
def business_owner_home(request):
    return render(request, 'pages/business_owner_home.html')