from django.urls import path
from .views import UserRegistrationView
from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path
from .views import FollowUnfollowView

urlpatterns = [
    path('follow/<int:user_id>/', FollowUnfollowView.as_view(), name='follow-unfollow'),
]