# Token处理与验证
import requests
import jwt
from decouple import config
import httpx

AUTHING_CONFIG = {
    'client_id': config('AUTHING_APP_ID'), # Authing应用ID
    'client_secret': config('AUTHING_APP_SECRET'), # Authing应用密钥
    'redirect_uri': config('AUTHING_APP_REDIRECT_URI'), # 登录回调地址
    'token_url': config('AUTHING_TOKEN_URL'), # TOKEN 令牌获取端点
    'jwks_url': config('AUTHING_JWKS_URL'), # JWKS公钥获取端点
    'issuer': config('AUTHING_ISSUER'),
    'user_info': config('AUTHING_USER_INFO'), # 用户信息端点
}

async def get_user_info(access_token):
    """
    使用Access Token 令牌从Authing获取用户信息
    """
    url = AUTHING_CONFIG['user_info']
    headers = {'Authorization': f'Bearer {access_token}'}
    
    # 创建异步HTTP客户端
    async with httpx.AsyncClient() as client:
        # 发起 GET 请求，等待响应完成
        response = await client.get(url, headers=headers)
        # 检查响应状态码
        response.raise_for_status() # 如果状态码非200,则抛出异常
        return response.json() # 返回JSON数据

async def get_token_from_authing(code):
    """
    使用授权码从 Authing 获取访问令牌和 ID token
    """
    data = {
        'grant_type': 'authorization_code',
        'client_id': AUTHING_CONFIG['client_id'],
        'client_secret': AUTHING_CONFIG['client_secret'],
        'code': code,
        'redirect_uri': AUTHING_CONFIG['redirect_uri'],
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(AUTHING_CONFIG['token_url'], data=data)
        response.raise_for_status()
        return response.json()

def verify_id_token(id_token):
    """
    验证 ID Token 合法性
    """
    try:
        jwks = requests.get(AUTHING_CONFIG['jwks_url']).json()
        header = jwt.get_unverified_header(id_token)
        rsa_key = next((key for key in jwks['keys'] if key['kid'] == header['kid']), None)
        
        if not rsa_key:
            raise Exception('未找到匹配的JWKS公钥')
        
        return jwt.decode(
            id_token,
            rsa_key,
            algorithms=['RS256'],
            audience=AUTHING_CONFIG['client_id'],
            issuer=AUTHING_CONFIG['issuer']
        )
    except Exception as e:
        raise Exception(f"ID Token 验证失败: {e}")