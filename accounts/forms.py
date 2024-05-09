from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model
from .models import Customer, BusinessOwner
from django.db import transaction

User = get_user_model()

class CustomerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','password1', 'password2']
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_number = self.cleaned_data.get('phone_number')
        customer.save()
        return user

class BusinessOwnerSignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15)
    address = forms.CharField(max_length=100)
    business_name = forms.CharField(max_length=100)
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'phone_number', 'address', 'business_name', 'password1', 'password2']
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_business_owner = True
        user.save()
        business_owner = BusinessOwner.objects.create(user=user)
        business_owner.phone_number = self.cleaned_data.get('phone_number')
        business_owner.address = self.cleaned_data.get('address')
        business_owner.business_name = self.cleaned_data.get('business_name')
        business_owner.save()
        return user
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
