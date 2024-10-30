# 自定义 JWT 认证类
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from tools.authing_token_utils import decode_jwt
from django.contrib.auth import get_user_model
from usermodule.models import UserProfile

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
            sub = decoded_token.get("sub")
            
            if not sub:
                raise AuthenticationFailed('Token 中缺少用户标识符')
            
            # 根据 sub 获取用户对象
            try:
                user = User.objects.get(sub=sub)
            except User.DoesNotExist:
                # 如果用户不存在,使用decoded_token创建用户
                user = User(
                    sub=sub,
                    phone_number=decoded_token.get('phone_number'),
                    phone_number_verified=decoded_token.get('phone_number_verified', False),
                    email=decoded_token.get('email'),
                    email_verified=decoded_token.get('email_verified', False),
                    username=decoded_token.get('username'),
                    is_active=True
                )
                user.save()
                
                # 创建用户资料
                profile = UserProfile(
                    user=user,
                    name=decoded_token.get('name'),
                    given_name=decoded_token.get('given_name'),
                    middle_name=decoded_token.get('middle_name'),
                    family_name=decoded_token.get('family_name'),
                    nickname=decoded_token.get('nickname'),
                    preferred_username=decoded_token.get('preferred_username'),
                    profile=decoded_token.get('profile'),
                    picture=decoded_token.get('picture'),
                    website=decoded_token.get('website'),
                    birthdate=decoded_token.get('birthdate'),
                    gender=decoded_token.get('gender'),
                    zoneinfo=decoded_token.get('zoneinfo'),
                    locale=decoded_token.get('locale'),
                    updated_at=decoded_token.get('updated_at')
                )
                profile.save()

            return (user, None)
        
        except Exception as e:
            raise AuthenticationFailed(f"Token 验证失败: {str(e)}")