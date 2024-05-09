from django.contrib import admin
from django.urls import path
from . import views
from accounts.views import CustomerSignUpView, BusinessOwnerSignUpView, LoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('customer_signup/', CustomerSignUpView.as_view(), name='customer_signup'),
    path('business_owner_signup/', BusinessOwnerSignUpView.as_view(), name='business_owner_signup'),
    path('login/', LoginView.as_view(), name='login'),

]
