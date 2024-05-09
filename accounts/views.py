from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView
from .models import CustomUser, Customer, BusinessOwner
from .forms import CustomerSignUpForm, BusinessOwnerSignUpForm, LoginForm
from django.contrib.auth import views as auth_views
from django.urls import reverse

# Create your views here.

def signup(request):
    return render(request, 'accounts/signup.html')


class CustomerSignUpView(CreateView):
    model = CustomUser
    form_class = CustomerSignUpForm
    template_name = 'accounts/customer_signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('pages:customer_home')

class BusinessOwnerSignUpView(CreateView):
    model = CustomUser
    form_class = BusinessOwnerSignUpForm
    template_name = 'accounts/business_owner_signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'business_owner'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('pages:business_owner_home')
    
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_customer:
                return reverse('customer_home')
            else:
                return reverse('business_owner_home')
        else:
            return reverse('login')
        
def signout(request):
    return render(request, 'accounts/signout.html')