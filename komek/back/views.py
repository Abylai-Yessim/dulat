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

    if request.method == 'POST':
        notification_form = UserNotificationForm(request.POST, initial={'organ': organ})
        if notification_form.is_valid():
            notification = notification_form.save(commit=False)
            notification.organ = organ  
            notification_form.save()
            messages.success(request, "Сообщение успешно отправлено.")
            
    else:
        notification_form = UserNotificationForm(initial={'organ': organ})

    return render(request, 'back/organ_details.html', {'organ': organ, 'notification_form': notification_form})

# def thank_page(request):
#     return render(request, 'back/thank_page.html')

def moderator_notifications(request):
    notifications = Notification.objects.all()
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
            
            if organ:
                comment.organ = organ
            else:
           
                comment.organ = Organ.objects.get(pk=1) 

            comment.user = request.user if request.user.is_authenticated else None
            comment.save()

        return redirect('back:comment')

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user == request.user or request.user.is_staff:
        comment.delete()
        return redirect('back:comment')
    else:
        return JsonResponse({'success': False, 'message': 'Permission denied'})