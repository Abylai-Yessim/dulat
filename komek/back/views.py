from django.shortcuts import render, render
from typing import Set
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .forms import *
import sys
sys.path.append("..")
from .models import *
from .forms import *
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import Http404

# Create your views here.

menu = [
    {'title': 'ikomek', 'url': 'back:home'},
]

def home(request):
    organs = Organ.objects.all()

    data = {
        'menu': menu,
        'title': 'Главная страница',
        'organs': organs, 
    }
    return render(request, 'back/home.html', context=data)

def organ_detail(request, organ_id):
    try:
        organ = Organ.objects.get(pk=organ_id)
    except Organ.DoesNotExist:
        raise Http404("Organ does not exist")

    notification_form = NotificationForm(request.POST or None, initial={'organ': organ})

    if request.method == 'POST' and notification_form.is_valid():
        notification = notification_form.save()
        messages.success(request, "Notification submitted successfully. A moderator will review it shortly.")
        return redirect('back:app_notification')

    return render(request, 'back/organ_details.html', {'organ': organ, 'notification_form': notification_form})

def notify_admin(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            notification = form.save(commit=False)
            print(f"Notification created: {notification}")
            print(f"Organ ID from form: {form.cleaned_data['organ'].id}")

            notification.save()
            messages.success(request, "New notification received!")
            return redirect('back:notify_admin')
    else:
        form = NotificationForm()

    return render(request, 'back/app_notification.html', {'form': form})



def thank_you_page(request):
    return render(request, 'back/app_notification.html')

def moderator_notifications(request):
    notifications = Notification.objects.all()
    print(f"Number of notifications: {len(notifications)}")
    for notification in notifications:
        if not notification.organ:
            print(f"Notification {notification.id} has no associated Organ.")
    print(f"Notifications data sent to the template: {notifications}")
    return render(request, 'back/moderator_notifications.html', {'notifications': notifications})



