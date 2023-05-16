from django.urls import path
from users.views import login, profile, logout, UserRegistrationView

app_name = 'users'

urlpatterns = [
  path('login/', login, name='login'), # ../users/login/
  path('registration/', UserRegistrationView.as_view(), name='registration'), # ../users/registration/
  path('profile/', profile, name='profile'), # ../users/registration/
  path('logout/', logout, name='logout'), # ../users/registration/
]