from django.urls import path
from .views import UserRegistrationView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),  # Endpoint for obtaining auth token

]