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
    authentication_classes = []  # 禁用认证类，确保这个视图不需要令牌
    permission_classes = []  # 禁用权限类
    
    def get(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            raise AuthenticationFailed("缺少或无有效的授权头!")
        
        try:
            token = auth_header.split()[1]
            user_info = async_to_sync(get_user_info)(token) # 异步转换为同步调用
            return Response(user_info, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"获取用户信息失败: {str(e)}"}, status=status.HTTP_401_UNAUTHORIZED)

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