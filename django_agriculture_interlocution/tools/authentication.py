# 自定义 JWT 认证类
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from tools.authing_token_utils import decode_jwt
from django.contrib.auth import get_user_model

User = get_user_model() # 获取自定义用户模型

class CustomJWTAuthentication(BaseAuthentication):
    """
    自定义 JWT 认证类, 使用封装的 decode_jwt函数。
    """
    # 从请求头中获取 Authorization
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        
        if not auth_header or not auth_header.startswith('Bearer '):
            raise AuthenticationFailed('缺少或无效的授权头')
        
        try:
            # 提取 Token 并解码
            token = auth_header.split(' ')[1]
            decoded_token = decode_jwt(token)
            user_id = decoded_token.get("sub")
            
            # 根据 user_id 获取用户对象
            try:
                user = User.objects.get(pk=user_id)
            except User.DoesNotExist:
                raise AuthenticationFailed('用户不存在')
            
            # 返回用户对象和None
            return (user, None)
        
        except Exception as e:
            raise AuthenticationFailed(f"Token 验证失败: {str(e)}")