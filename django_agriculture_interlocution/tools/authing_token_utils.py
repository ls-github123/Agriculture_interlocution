# 封装 Token 处理与验证方法
# 令牌及用户信息获取
import jwt
from jwt import PyJWKClient
import requests
from decouple import config
import httpx
from cachetools import cached, TTLCache

AUTHING_CONFIG = {
    'client_id': config('AUTHING_APP_ID'), # Authing应用ID
    'client_secret': config('AUTHING_APP_SECRET'), # Authing应用密钥
    'redirect_uri': config('AUTHING_APP_REDIRECT_URI'), # 登录回调地址
    'token_url': config('AUTHING_TOKEN_URL'), # TOKEN 令牌获取端点
    'jwks_url': config('AUTHING_JWKS_URL'), # JWKS公钥获取端点
    'issuer': config('AUTHING_ISSUER'), # 令牌颁发者 (Issuer)
    'user_info': config('AUTHING_USER_INFO'), # 用户信息端点
}

# 缓存JWKS公钥 -- 避免重复请求 Authing JWKS 端点
# maxsize 缓存中允许存储的最大条目
# ttl -- time to live 生存时间
jwsk_cache = TTLCache(maxsize=1, ttl=3600 * 24 * 7)

# 使用python3中的 -> PyJWKClient 类型注解 明确函数返回值类型
@cached(jwsk_cache)
def get_jwks_client() -> PyJWKClient:
    """
    获取 JWKS 客户端公钥并缓存,时间7天。
    """
    return PyJWKClient(AUTHING_CONFIG['jwks_url'])

def decode_jwt(token):
    """
    解码并验证 JWT, 返回解码后的 payload。
    """
    jwks_client = get_jwks_client()
    # JWKS 客户端根据传入的 JWT，找到用于签名的 公钥
    signing_key = jwks_client.get_signing_key_from_jwt(token)
    data = jwt.decode(
        token, # 传入的 JWT 字符串
        key=signing_key.key, # 使用从 JWKS 中找到的公钥来解码和验证 JWT 签名
        algorithms=["RS256"], # 指定支持的加密算法
        # 确保令牌的 aud(audience，接收方) 字段与应用的 client_id 匹配 (防止令牌被错误的应用使用)
        audience=AUTHING_CONFIG['client_id'],
        options={"verify_exp": True} # 开启对令牌过期时间的验证(exp 过期时间字段)
    )
    # print(f"打印JWT解码后的令牌payload:{data}")
    return data # 将解码后的 payload 返回给调用者

async def get_token_from_authing(code: str) -> dict:
    """
    使用授权码从 Authing 获取 Access Token \ ID Token \ Refresh Token。
    """
    data = {
        'grant_type': 'authorization_code',
        'client_id': AUTHING_CONFIG['client_id'],
        'client_secret': AUTHING_CONFIG['client_secret'],
        'code': code,
        'redirect_uri': AUTHING_CONFIG['redirect_uri'],
        'scope': 'openid profile email offline_access',
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(AUTHING_CONFIG['token_url'], data=data)
            response.raise_for_status()
            return response.json() # 返回令牌信息(包括 access_token\id_token\refresh_token)
        except httpx.HTTPStatusError as e:
            raise Exception(f"获取令牌失败: {e.response.status_code} - {e.response.text}")
        
async def get_user_info(access_token: str) -> dict:
    """
    使用 Access Token 从 Authing 获取用户信息
    """
    headers = {'Authorization': f'Bearer {access_token}'}
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(AUTHING_CONFIG['user_info'], headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise Exception(f"获取用户信息失败: {e.response.status_code} - {e.response.text}")
        
async def refresh_Authing_token(refresh_token: str) -> dict:
    """
    使用 Refresh Token 从 Authing 获取新的 Access Token。
    """
    data = {
        'grant_type': 'refresh_token',
        'client_id': AUTHING_CONFIG['client_id'],
        'client_secret': AUTHING_CONFIG['client_secret'],
        'refresh_token': refresh_token,
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(AUTHING_CONFIG['token_url'], data=data)
            response.raise_for_status()
            return response.json() # 返回新的 Access Token 和 Refresh Token
        except httpx.HTTPStatusError as e:
            raise Exception(f"刷新 Access Token 失败: {e.response.status_code} - {e.response.text}")