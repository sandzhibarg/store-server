from django.contrib.auth.forms import AuthenticationForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    class Meta: # Класс мета принимает дополнительные параметры,которые указываем ниже
        model = User
        fields = ('username', 'password')