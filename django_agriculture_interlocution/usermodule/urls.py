from django.urls import path
from .views import protected_view

urlpatterns = [
    path('dashboard/', protected_view), # 受保护的API
]
