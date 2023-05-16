from django.urls import path
from users.views import login, logout, UserRegistrationView, UserProfileView

app_name = 'users'

urlpatterns = [
  path('login/', login, name='login'), # ../users/login/
  path('registration/', UserRegistrationView.as_view(), name='registration'), # ../users/registration/
  path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'), # ../users/registration/
  path('logout/', logout, name='logout'), # ../users/registration/
]