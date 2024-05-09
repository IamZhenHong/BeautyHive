from django.contrib import admin
from .models import Customer, BusinessOwner, CustomUser
# Register your models here.

admin.site.register(Customer)
admin.site.register(BusinessOwner)
admin.site.register(CustomUser)