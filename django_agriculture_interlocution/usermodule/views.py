from django.views.decorators.csrf import csrf_protect # 导入 csrf_protect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from asgiref.sync import async_to_sync # 导入 async_to_sync
from .authin_utils import get_token_from_authing, get_user_info
import jwt
import requests
import httpx

@csrf_protect # 确保请求经过 CSRF 保护
@api_view(['POST'])
def exchange_token(request):
    """
    处理授权码并获取访问令牌和用户信息
    """
    code = request.data.get('code') # 从请求体中获取授权码
    print(f"获取的授权码: {code}")
    if not code:
        return Response({'error': '缺少授权码'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # 使用 async_to_sync 包装异步调用
        # 使用授权码从 Authing 获取访问令牌
        token_data = async_to_sync(get_token_from_authing)(code)
        # print(f"打印Token_data:{token_data}")
        access_token = token_data.get('access_token') # 
        id_token = token_data.get('id_token')
        
        if not id_token:
            return Response({'error': 'ID Token 不存在'}, status=status.HTTP_400_BAD_REQUEST)
        
        # 使用 async_to_sync 包装异步获取用户信息
        user_info = async_to_sync(get_user_info)(access_token)
        
        return Response({
            'user_info': user_info,
            'access_token': token_data.get('access_token'),
        }, status=status.HTTP_200_OK)
    
    except httpx.RequestError as e:
        return Response({'error': f'网络请求失败: {str(e)}'}, status=status.HTTP_502_BAD_GATEWAY)

    except jwt.ExpiredSignatureError:
        return Response({'error': '令牌已过期'}, status=status.HTTP_401_UNAUTHORIZED)

    except jwt.InvalidTokenError:
        return Response({'error': '无效的令牌'}, status=status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return Response({'error': f'未知错误: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def user_info(request):
    authorization_header = request.headers.get('Authorization')
    
    if not authorization_header:
        return Response({'error': '缺少访问令牌'}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        token = authorization_header.split()[1]
        user_info = async_to_sync(get_user_info)(token)
        
        return Response(user_info, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({'error': f'未知错误: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)