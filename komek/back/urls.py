from django.urls import path, include
from . import views 
from .views import *
app_name = 'back'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:organ_id>/', organ_detail, name='organ_detail'),
]