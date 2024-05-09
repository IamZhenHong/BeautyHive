from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_customer = models.BooleanField(default=False)
    is_business_owner = models.BooleanField(default=False)
    
    class Meta:
        app_label = 'accounts'  # Specify the name of your Django app

# Specify related_name in ManyToManyField to resolve clashes
CustomUser.groups.field.related_name = 'custom_user_groups'
CustomUser.user_permissions.field.related_name = 'custom_user_permissions'

class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.email
    

class BusinessOwner(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100)


    def __str__(self):
        return self.user.email