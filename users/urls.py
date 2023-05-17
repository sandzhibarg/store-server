from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import (EmailVerificationView, UserloginView, UserProfileView,
                         UserRegistrationView)

app_name = 'users'

urlpatterns = [
  path('login/', UserloginView.as_view(), name='login'), # ../users/login/
  path('registration/', UserRegistrationView.as_view(), name='registration'), # ../users/registration/
  path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'), # ../users/registration/
  path('logout/', LogoutView.as_view(), name='logout'), # ../users/registration/
  path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),
]