from django.shortcuts import render, render
from typing import Set
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .forms import *
import sys
sys.path.append("..")
from .models import *
from .forms import *

from django.shortcuts import get_object_or_404

# Create your views here.

menu = [
    {'title': 'ikomek', 'url': 'back:home'},
]

def home(request):
    organs = Organ.objects.all()
    notification_form = NotificationForm(request.POST or None)
    if request.method == 'POST' and notification_form.is_valid():
        notification = notification_form.save()

    data = {
        'menu': menu,
        'title': 'Главная страница',
        'organs': organs, 
        'notification_form': notification_form,
    }
    return render(request, 'back/home.html', context=data)


def organ_detail(request, organ_id):
    
    organ = get_object_or_404(Organ, pk=organ_id)
    notification_form = NotificationForm(request.POST or None)

    if request.method == 'POST' and notification_form.is_valid():
        
        notification = notification_form.save()
       
        return redirect('back:organ_detail', organ_id=organ_id)
    

    return render(request, 'back/organ_details.html', {'organ': organ, 'notification_form': notification_form})