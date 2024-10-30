from django.urls import path
from .views import *

urlpatterns = [
    path('service-messages/', ServiceNotificationList.as_view(), name='service-messages-list'),
    path('weather-reminders/', WeatherReminderList.as_view(), name='weather-reminders-list'),
    path('planting-messages/', PlantingMessageList.as_view(), name='planting-messages-list'),
    path('praise-comment-messages/', PraiseCommentMessageList.as_view(), name='praise-comment-messages-list'),
    path('system-notifications/', SystemNotificationList.as_view(), name='system-notifications-list'),
    path('mark-as-read/', MarkAsReadView.as_view(), name='mark-as-read'),

   # 新增的单个消息详情路由
    path('service-messages/<int:pk>/', ServiceNotificationDetail.as_view(), name='service-notification-detail'),
    path('weather-reminders/<int:pk>/', WeatherReminderDetail.as_view(), name='weather-reminder-detail'),
    path('planting-messages/<int:pk>/', PlantingMessageDetail.as_view(), name='planting-message-detail'),
    path('praise-comment-messages/<int:pk>/', PraiseCommentMessageDetail.as_view(), name='praise-comment-message-detail'),
    path('system-notifications/<int:pk>/', SystemNotificationDetail.as_view(), name='system-notification-detail'),
]
