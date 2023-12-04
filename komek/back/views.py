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
from django.views.generic.detail import DetailView
from django.http import JsonResponse
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

            notification.save()

            messages.success(request, "Notification submitted successfully.")
            print("Redirecting to moderator_notifications")
            return redirect('back:moderator_notifications')  
        else:
            print(f"Form errors: {form.errors}")
            messages.error(request, "Form submission failed. Please check the errors.")
    else:
        form = NotificationForm()

    organs = Organ.objects.all()
    return render(request, 'back/app_notification.html', {'form': form, 'organs': organs})


def thank_you_page(request):
    return render(request, 'back/app_notification.html')

def moderator_notifications(request):
    print("Inside moderator_notifications view")
    notifications = Notification.objects.all()
    print("Notifications:", notifications)  # Check the printed output in your console
    return render(request, 'back/moderator_notifications.html', {'notifications': notifications})

class CommentDetail(DetailView):
    model = Organ
    template_name = 'back/comment.html'
    context_object_name = 'organ'
    pk_url_kwarg = 'organ_id'

    def get_object(self, queryset=None):
        organ_id = self.kwargs.get('organ_id')
        if organ_id:
            return super().get_object(queryset)
        else:
            # Return a dummy Organ object (you can customize this)
            return Organ()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Отзывы'
        
        organ_id = self.kwargs.get('organ_id')
        if organ_id:
            context['comments'] = Comment.objects.filter(organ_id=organ_id)
        else:
            context['comments'] = Comment.objects.all()

        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        organ_id = self.kwargs.get('organ_id')
        organ = Organ.objects.get(pk=organ_id) if organ_id else None

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            
            # Check if organ is not None before associating it with the comment
            if organ:
                comment.organ = organ
            else:
                # Handle the case where organ is None (you can customize this)
                comment.organ = Organ.objects.get(pk=1)  # Use a default Organ instance or adjust as needed

            comment.user = request.user if request.user.is_authenticated else None
            comment.save()

        return redirect('back:comment')

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Check if the user is the author of the comment or a staff member
    if comment.user == request.user or request.user.is_staff:
        comment.delete()
        return redirect('back:comment')
    else:
        return JsonResponse({'success': False, 'message': 'Permission denied'})