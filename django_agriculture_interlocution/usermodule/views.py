from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from asgiref.sync import async_to_sync # 导入 async_to_sync
from tools.authing_token_utils import get_user_info, get_token_from_authing, refresh_Authing_token
from rest_framework.exceptions import AuthenticationFailed

class ExchangeToken(APIView):
    """
    使用授权码获取 Access Token 和 ID Token。
    """
    
    authentication_classes = []  # 禁用认证类，确保这个视图不需要令牌
    permission_classes = []  # 禁用权限类
    def post(self, request):
        code = request.data.get('code')
        if not code:
            return Response({"error":"未获取到授权码"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            tokens = async_to_sync(get_token_from_authing)(code) # 使用授权码获取令牌
            print(f"令牌数据已获取")
            return Response(tokens, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"获取令牌失败:{str(e)}"}, status=status.HTTP_401_UNAUTHORIZED)

class UserInfoView(APIView):
    """
    使用 Access Token 获取用户信息。
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        profile = user.profile
        
        data = {
            'sub': user.sub,
            'phone_number': user.phone_number,
            'phone_number_verified': user.phone_number_verified,
            'email': user.email,
            'email_verified': user.email_verified,
            'username': user.username,
            'name': profile.name,
            'given_name': profile.given_name,
            'middle_name': profile.middle_name,
            'family_name': profile.family_name,
            'nickname': profile.nickname,
            'preferred_username': profile.preferred_username,
            'profile': profile.profile,
            'picture': profile.picture,
            'website': profile.website,
            'birthdate': profile.birthdate,
            'gender': profile.gender,
            'zoneinfo': profile.zoneinfo,
            'locale': profile.locale,
            'updated_at': profile.updated_at.isoformat() if profile.updated_at else None
        }
        
        return Response(data)


class RefreshTokenView(APIView):
    """
    接收 refresh_token, 并返回新的 access_token 和 id_token
    """
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        
        if not refresh_token:
            return Response({"error": "缺少refresh_token"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # 调用封装的 Authing 逻辑刷新令牌
            tokens = async_to_sync(refresh_Authing_token)(refresh_token)
            
            return Response({
                "access_token": tokens.get("access_token"),
                "id_token": tokens.get("id_token"),
                "expires_in": tokens.get("expires_in"),
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
    

class JwtTestView(APIView):
    """
    测试JWT鉴权接口
    """
    permission_classes = [IsAuthenticated] # 确保只有认证用户可以访问
    
    def get(self, request):
        return Response({
            "message": "JWT认证成功!"
        }, status=status.HTTP_200_OK)