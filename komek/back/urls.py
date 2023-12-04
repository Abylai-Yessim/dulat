from django.urls import path, include
from . import views 
from .views import *
app_name = 'back'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:organ_id>/', views.organ_detail, name='organ_detail'), 
    path('comment/', views.CommentDetail.as_view(), name='comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('moderator-notifications/', views.moderator_notifications, name='moderator_notifications'),
    path('thank-page/', views.thank_page, name='thank_page'),
]
