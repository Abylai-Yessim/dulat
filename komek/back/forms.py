from django import forms
from .models import *
from django.core.validators import RegexValidator

class UserNotificationForm(forms.ModelForm):
    phone_number = forms.CharField(validators=[RegexValidator(regex=r'^\d{10}$', message='Enter a valid phone number.')])

    class Meta:
        model = Notification
        fields = ['name', 'address', 'phone_number']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']