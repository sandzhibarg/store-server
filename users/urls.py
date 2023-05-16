from django.urls import path
from users.views import UserloginView, logout, UserRegistrationView, UserProfileView
from django.contrib.auth.decorators import login_required

app_name = 'users'

urlpatterns = [
  path('login/', UserloginView.as_view(), name='login'), # ../users/login/
  path('registration/', UserRegistrationView.as_view(), name='registration'), # ../users/registration/
  path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'), # ../users/registration/
  path('logout/', logout, name='logout'), # ../users/registration/
]