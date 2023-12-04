from django import forms
from .models import *

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['organ', 'name', 'address', 'phone_number']
        widgets = {
            'organ': forms.Select(),  
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']