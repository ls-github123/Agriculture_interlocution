"""
ASGI config for django_agriculture_interlocution project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import websocket_model.routing

# 设置 Django 环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_agriculture_interlocution.settings')

# ASGI 应用程序
application = ProtocolTypeRouter({
    "http": get_asgi_application(), # 处理 HTTP 请求
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_model.routing.websocket_urlpatterns # 路由 WebSocket 请求
        )
    ),
})
