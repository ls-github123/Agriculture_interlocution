from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.ChatRoomListCreateView.as_view(), name='chat-room-list-create'),
    path('rooms/<str:room_name>/history', views.ChatHistoryView.as_view(), name='chat-history'),
]
