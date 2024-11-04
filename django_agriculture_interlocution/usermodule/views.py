from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from asgiref.sync import async_to_sync # 导入 async_to_sync
from tools.authing_token_utils import get_user_info, get_token_from_authing, refresh_Authing_token, decode_jwt
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from usermodule.models import UserProfile, UsersModel, UserVerification
from .real_identity_verify import check_id_card # 身份证实名认证封装
from decouple import config
import re

class ExchangeToken(APIView):
    """
    使用授权码获取 Access Token \ ID Token \ Refresh Token。
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

User = get_user_model()

class UserInfoView(APIView):
    """
    使用 Access Token 获取用户信息。
    """
    permission_classes = [IsAuthenticated] # 确保只有认证用户可以访问
    
    def get(self, request):
        # 从 request.user 获取用户唯一标识符 sub
        # 直接从自定义认证类中获取解码的令牌载荷 sub 信息
        user_sub = request.user.sub
        
        # 从数据库获取用户实例
        user_instance = get_object_or_404(UsersModel, sub=user_sub)

        # 从请求头中获取 access_token
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return Response({'detail': '缺少或无效的授权头'}, status=status.HTTP_401_UNAUTHORIZED)
        
        access_token = auth_header.split(' ')[1]

        # 调用异步的 get_user_info 函数
        try:
            user_info = async_to_sync(get_user_info)(access_token)
        except Exception as e:
            return Response({'detail': f'获取用户信息失败：{str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if user_info:
            # 更新用户实例的主要信息
            user_instance.phone_number = user_info.get('phone_number', user_instance.phone_number)
            user_instance.phone_number_verified = user_info.get('phone_number_verified', user_instance.phone_number_verified)
            user_instance.email = user_info.get('email', user_instance.email)
            user_instance.email_verified = user_info.get('email_verified', user_instance.email_verified)
            user_instance.username = user_info.get('username', user_instance.username)
            user_instance.save()

            # 更新用户的扩展资料
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

            UserProfile.objects.update_or_create(
                user = user_instance,
                defaults = profile_data
            )

        # 准备返回数据
        profile = getattr(user_instance, 'profile', None)
        data = {
            'sub': user_instance.sub,
            'phone_number': user_instance.phone_number,
            'phone_number_verified': user_instance.phone_number_verified,
            'email': user_instance.email,
            'email_verified': user_instance.email_verified,
            'username': user_instance.username,
            'is_verified': user_instance.is_verified  # 用户是否实名 仅返回，不修改
        }

        # 如果用户有扩展资料，将其附加到响应数据
        if profile:
            data.update({
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
            })

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

class VerifyIdCardView(APIView):
    """
    身份证二要素(姓名+身份证号)实名认证接口。
    """
    permission_classes = [IsAuthenticated] # 确保只有认证用户可访问
    
    def post(self, request):
        # 直接从 request.user 获取用户 sub 信息
        user_sub = request.user.sub
        
        # 获取请求数据
        name = request.data.get('name')
        idcard = request.data.get('idcard')
        appcode = config('VERIFY_IDCARD_APPCODE') # 接口AppCode
        
        # 验证必填字段
        if not name or not idcard:
            return Response({'error': '用户姓名和身份证号不能为空!'}, status=status.HTTP_400_BAD_REQUEST)
        
        # 正则校验输入信息
        # 姓名校验 中文字符 长度1-20
        name_pattern = r'^[\u4e00-\u9fa5]{1,20}$'
        # 身份证号校验: 18位纯数字或17位数字加X/x
        idcard_pattern = r'^\d{17}[\dXx]$'
        
        if not re.match(name_pattern, name):
            return Response({'error': '输入的用户姓名无效!'}, status=status.HTTP_400_BAD_REQUEST)
        if not re.match(idcard_pattern, idcard):
            return Response({'error': '输入的身份证号格式无效!'}, status=status.HTTP_400_BAD_REQUEST)
        
        # 调用异步 check_id_card 函数 转换为同步调用
        try:
            result = async_to_sync(check_id_card)(name, idcard, appcode)
        except Exception as e:
            return Response({'error': f'验证身份证信息失败: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        # 解析结果并处理
        if result and result.get('success') and result.get('code') == 200:
            data = result.get('data', {})
            
            # 检查验证结果(0表示一致， 1表示不一致)
            if data.get('result') == 0:
                # 验证成功, 更新用户信息
                user_instance = get_object_or_404(UsersModel, sub=user_sub)
                user_instance.is_verified = True
                user_instance.save()
                
                # 保存用户实名信息
                UserVerification.objects.update_or_create(
                    user = user_instance,
                    defaults = {
                        'real_name':name,
                        'id_card_number': idcard
                    }
                )
                
                # 准备成功响应数据
                return Response({
                    'msg': '身份验证成功',
                    'user_data': {
                        'birthday': data.get('birthday'),
                        'address': data.get('address'),
                        'sex': data.get('sex'),
                        'order_no': data.get('orderNo')
                    }
                }, status=status.HTTP_200_OK)
            else:
                # 验证不一致
                return Response({
                    'msg': '身份验证失败!',
                    'description': data.get('desc', '不一致')
                }, status=status.HTTP_400_BAD_REQUEST)
        
        # 如果返回的 success 为 False 或 code 不是 200
        return Response({'error': '用户身份信息验证失败!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class JwtTestView(APIView):
    """
    测试JWT鉴权接口
    """
    permission_classes = [IsAuthenticated] # 确保只有认证用户可以访问
    
    def get(self, request):
        # 直接使用 request.user.sub 获取用户令牌载荷的 sub 信息
        user_sub = request.user.sub
        print(user_sub, type(user_sub))
        
        # request_user_sub = request.user
        # print(request_user_sub, type(request_user_sub))
        
        return Response({
            "message": "JWT认证成功!",
            'sub': f'用户sub为:{user_sub}'
        }, status=status.HTTP_200_OK)