from django.urls import path
from .views import exchange_token, user_info

urlpatterns = [
    path('token/', exchange_token, name='exchange-token'), # 获取令牌
    path('info/', user_info, name='user_info'), # 后续获取用户信息
]
