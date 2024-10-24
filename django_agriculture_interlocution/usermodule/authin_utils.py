# 初始化Authing身份云模块
from authing import AuthenticationClient
from decouple import config

# 初始化 AuthenticationClient
authentication_client = AuthenticationClient(
    # Authing 应用ID
    app_id = config('AUTHING_APP_ID'),
    
    # Authing 应用密钥
    app_secret = config('AUTHING_APP_SECRET'),
    
    # Authing应用地址
    app_host = config('AUTHING_APP_HOST'),
    
    # Authing应用登录回调地址
    # redirect_uri = config('AUTHING_APP_REDIRECT_URI'),
)

