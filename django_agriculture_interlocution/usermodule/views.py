from django.http import JsonResponse
from .utils import verify_jwt

def protected_view(request):
    """受保护的 API:仅允许持有合法 JWT 的用户访问。"""
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    
    if not auth_header or not auth_header.startswith('Bearer '):
        return JsonResponse({'error': '缺少授权头或格式错误'}, status=401)

    token = auth_header.split(' ')[1]

    try:
        user_info = verify_jwt(token)  # 验证并解析 JWT
        return JsonResponse({
            'message': '欢迎访问用户控制面板',
            'user_info': user_info,
        })
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=401)