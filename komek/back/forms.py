from django import forms
from .models import *

class UserNotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['name', 'address', 'phone_number', 'description']

        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-dess'}),
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

