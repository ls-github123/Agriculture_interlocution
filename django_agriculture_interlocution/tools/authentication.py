# 自定义 JWT 认证类
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from tools.authing_token_utils import decode_jwt
from django.contrib.auth import get_user_model
from tools.authing_token_utils import get_user_info
from asgiref.sync import async_to_sync # 导入 async_to_sync
from usermodule.models import UserProfile

User = get_user_model()

class CustomJWTAuthentication(BaseAuthentication):
    """
    自定义 JWT 认证类, 验证令牌并返回用户对象。
    """
    # 从请求头中获取 Authorization
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        
        if not auth_header or not auth_header.startswith('Bearer '):
            return None # 返回 None，DRF处理未认证的情况
        
        token = auth_header.split(' ')[1]
        
        try:
            decode_token = decode_jwt(token)
        except Exception as e:
            raise AuthenticationFailed(f"令牌验证失败: {str(e)}")
        
        sub = decode_token.get("sub")
        if not sub:
            raise AuthenticationFailed('令牌中缺少用户标识符(sub)!')
        
        # 尝试获取用户
        try:
            user = User.objects.get(sub=sub)
            return (user, None)
        except User.DoesNotExist:
            # 从 Authing 获取用户详细信息
            user_info = async_to_sync(get_user_info)(token)
            if not user_info:
                raise AuthenticationFailed('无法从 Authing 获取用户信息。')

            phone_number = user_info.get('phone_number')
            if not phone_number:
                raise AuthenticationFailed('用户信息中缺少手机号（phone_number）。')

            # 创建用户
            user = User.objects.create_user(
                sub=sub,
                phone_number=phone_number,
                phone_number_verified=user_info.get('phone_number_verified', False),
                email=user_info.get('email'),
                email_verified=user_info.get('email_verified', False),
                username=user_info.get('username'),
                is_active=True,
                is_staff=False
            )
            
            # 创建用户资料
            profile_data = {
                'name': user_info.get('name'),
                'given_name': user_info.get('given_name'),
                'middle_name': user_info.get('middle_name'),
                'family_name': user_info.get('family_name'),
                'nickname': user_info.get('nickname'),
                'preferred_username': user_info.get('preferred_username'),
                'profile': user_info.get('profile'),
                'picture': user_info.get('picture'),
                'website': user_info.get('website'),
                'birthdate': user_info.get('birthdate'),
                'gender': user_info.get('gender'),
                'zoneinfo': user_info.get('zoneinfo'),
                'locale': user_info.get('locale'),
                'updated_at': user_info.get('updated_at')
            }
            UserProfile.objects.create(
                user=user,
                **profile_data
            )

        return (user, None)