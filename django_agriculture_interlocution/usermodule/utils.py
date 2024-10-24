# JWT 验证
import jwt
import jwt.algorithms
import requests
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError, DecodeError
from decouple import config

# JWKS 公钥端点
JWKS_URL = "https://agriculture-interlocution.authing.cn/oidc/.well-known/jwks.json"

def get_public_key(kid):
    """
    从Authing获取JWKS公钥,并得到对应KID
    """
    response = requests.get(JWKS_URL)
    jwks = response.json()
    
    for key in jwks['keys']:
        if key['kid'] == kid:
            return jwt.algorithms.RSAAlgorithm.from_jwk(key)
    raise ValueError("Invalid KID: 公钥未找到")

def verify_jwt(token):
    """
    验证JWT令牌的合法性及签名
    """
    try:
        headers = jwt.get_unverified_header(token)
        kid = headers['kid']
        public_key = get_public_key(kid)
        
        decoded = jwt.decode(
            token,
            public_key,
            algorithms = ["RS256"],
            audience = config('AUTHING_APP_ID'),
            issuer = config('AUTHING_ISSUER')
        )
        return decoded
    except ExpiredSignatureError:
        raise ValueError("令牌已过期")
    except InvalidSignatureError:
        raise ValueError("无效的令牌签名")
    except DecodeError:
        raise ValueError("令牌解析失败")
    except Exception as e:
        raise ValueError(f"验证过程中发生错误: {str(e)}")