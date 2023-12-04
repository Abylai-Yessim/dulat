from django.urls import path, include
from . import views 
from .views import *
app_name = 'back'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:organ_id>/', organ_detail, name='organ_detail'),
    path('app-notification/', thank_you_page, name='app_notification'),
    path('comment/', CommentDetail.as_view(), name='comment'),
    path('comment/delete/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('notify-admin/', notify_admin, name='notify_admin'),
    path('moderator-notifications/', moderator_notifications, name='moderator_notifications'),
]