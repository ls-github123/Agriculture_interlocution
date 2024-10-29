from django.urls import path
from .views import ExchangeToken, UserInfoView, RefreshTokenView, JwtTestView

urlpatterns = [
    path('token/', ExchangeToken.as_view(), name='exchange-token'), # 获取令牌
    path('refresh_token/', RefreshTokenView.as_view(), name='refresh_token'), # 刷新令牌
    path('user_info/', UserInfoView.as_view(), name='user_info'), # 后续获取用户信息
    path('test_jwt/', JwtTestView.as_view(), name='jwt_test'), # 测试JWT鉴权 
]
