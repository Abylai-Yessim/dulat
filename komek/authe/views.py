from typing import Set
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import *
import sys
sys.path.append("..")
from back.models import *
from back.forms import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.

menu = [
    {'title': 'iKomek', 'url': 'back:home'},
]

class SignUpUser(CreateView):
    form_class = SignUpUserForm
    template_name = 'back/signup.html'
    success_url = reverse_lazy('back:profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Регистрация'
        context['menu'] = menu

        return context
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('back:home')
    

class SignInUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'back/signin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Вход'
        context['menu'] = menu

        return context
    
    def get_success_url(self):
        return reverse_lazy('back:profile')
    

    
def signout_user(request):
    logout(request)
    return redirect('back:home')





