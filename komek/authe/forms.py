from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class SignUpUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
        }

        labels = {
            'username': _('Имя пользователя'),
            'email': _('Электронная почта'),
            'first_name': _('Имя'),
            'last_name': _('Фамилия'),
            'password1': _('Пароль'),
            'password2': _('Подтверждение пароля'),
        }

        help_texts = {
            'password1': _('Ваш пароль должен содержать...'),
            'password2': _('Пожалуйста, повторите пароль для подтверждения.'),
        }

class SignInUserForm(AuthenticationForm):
    username = forms.CharField(label=_('Имя пользователя'), widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password')

        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-input'}),
        }

        labels = {
            'password': _('Пароль'),
        }

        help_texts = {
            'password': _('Пожалуйста, введите ваш пароль.'),
        }
