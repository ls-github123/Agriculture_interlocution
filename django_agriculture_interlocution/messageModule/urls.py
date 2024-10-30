from django.urls import path
from .views import *

urlpatterns = [
    path('service-messages/', ServiceNotificationList.as_view(), name='service-messages-list'),
    path('weather-reminders/', WeatherReminderList.as_view(), name='weather-reminders-list'),
    path('planting-messages/', PlantingMessageList.as_view(), name='planting-messages-list'),
    path('praise-comment-messages/', PraiseCommentMessageList.as_view(), name='praise-comment-messages-list'),
    path('system-notifications/', SystemNotificationList.as_view(), name='system-notifications-list'),
    path('mark-as-read/', MarkAsReadView.as_view(), name='mark-as-read'),

   
]
