from django.contrib.auth.forms import AuthenticationForm
from django import forms

from users.models import User

class UserLoginForm(AuthenticationForm):
    # добавляем наши стили для формы в login.html для поля ввода имя пользователя
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    # добавляем свои стили для формы ввода пароля
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    class Meta: # Класс мета принимает дополнительные параметры,которые указываем ниже
        model = User
        fields = ('username', 'password')