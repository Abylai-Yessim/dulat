from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import UserProfile, CustomUser

class SignUpUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'lastname', 'username', 'address', 'phone_number', 'password1', 'password2')

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'lastname': forms.TextInput(attrs={'class': 'form-input'}),
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'address': forms.TextInput(attrs={'class': 'form-input'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }

class SignInUserForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password': forms.PasswordInput(attrs={'class': 'form-input'}),
        }