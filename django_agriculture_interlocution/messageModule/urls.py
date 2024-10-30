from django.urls import path
from .views import *

urlpatterns = [
    # 服务通知列表路由
    path('service-messages/', ServiceNotificationList.as_view(), name='service-messages-list'),
    
    # 天气提醒列表路由
    path('weather-reminders/', WeatherReminderList.as_view(), name='weather-reminders-list'),
    
    # 种植信息列表路由
    path('planting-messages/', PlantingMessageList.as_view(), name='planting-messages-list'),
    
    # 赞评论信息列表路由
    path('praise-comment-messages/', PraiseCommentMessageList.as_view(), name='praise-comment-messages-list'),
    
    # 系统通知列表路由
    path('system-notifications/', SystemNotificationList.as_view(), name='system-notifications-list'),
    
    # 标记消息为已读的路由
    path('mark-as-read/', MarkAsReadView.as_view(), name='mark-as-read'),
    
    # 新增的单个消息详情路由
    path('service-messages/<int:pk>/', ServiceNotificationDetail.as_view(), name='service-notification-detail'),
    path('weather-reminders/<int:pk>/', WeatherReminderDetail.as_view(), name='weather-reminder-detail'),
    path('planting-messages/<int:pk>/', PlantingMessageDetail.as_view(), name='planting-message-detail'),
    path('praise-comment-messages/<int:pk>/', PraiseCommentMessageDetail.as_view(), name='praise-comment-message-detail'),
    path('system-notifications/<int:pk>/', SystemNotificationDetail.as_view(), name='system-notification-detail'),
]