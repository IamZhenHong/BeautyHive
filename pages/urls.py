from django.contrib import admin
from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('customer_home/', views.customer_home, name='customer_home'),
    path('business_owner_home/', views.business_owner_home, name='business_owner_home'),

]
