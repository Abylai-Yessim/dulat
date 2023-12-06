from django import forms
from .models import *

class UserNotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['name', 'address', 'phone_number', 'description']

        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-dess'}),
        }

        labels = {
            'name': 'Имя',
            'address': 'Адрес',
            'phone_number': 'Номер телефона',
            'description': 'Описание',
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        labels = {
            'text': 'Текст',
        }

