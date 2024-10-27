from django.urls import path
from .views import message_list,message_detail

urlpatterns = [
    path('messages/', message_list, name='message_list'),
    path('messages/<int:message_id>/', message_detail, name='message_detail'),
]


