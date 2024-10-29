"""
Django settings for django_agriculture_interlocution project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
# python-decouple包, 导入本地.env配置信息(mysql数据库地址、密码、端口等),该信息不会被git同步
from decouple import config
import os
from datetime import timedelta
from tools.authing_token_utils import get_jwks_client # 导入获取JWKS公钥函数
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#wm$u&@(9*z=wbzh$r$!zl^5jscyjl==^4q$a71zwi$xv%ux_s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True # 配置跨域,允许所有访问

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders', # 跨域配置
    'rest_framework', # DRF支持
    'usermodule', # 子应用-用户模块
]



# 设置Django AUTH 用户认证系统所需用户模型
# 格式: 子应用名.模型名  -- 必须在数据第一次迁移时配置完成
AUTH_USER_MODEL = "usermodule.UsersModel"

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # CORS处理
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', # 启用 CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 跨域请求设置
# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:5173',
# ]

CORS_ALLOW_CREDENTIALS = True  # 允许发送 Cookie

# CSRF 信任来源
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:5173'
]

ROOT_URLCONF = 'django_agriculture_interlocution.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_agriculture_interlocution.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# 数据库配置，使用mysqlclient
DATABASES = {
    'default': { # config 从.env文件中读取mysql机密配置信息
        "ENGINE":"django.db.backends.mysql", # 使用nei的 MySQL 引擎
        "NAME": config('DB_NAME'), # 数据库名称
        "USER": config('DB_USER'), # 数据库用户
        "PASSWORD": config('DB_PASSWORD'), # 数据库密码
        "HOST": config('DB_HOST', default='localhost'), # 数据库主机地址
        "PORT": config('DB_PORT', default='3306'), # 数据库端口
        "OPTIONS": { # 数据库连接高级选项
            # init_command 初始化连接时执行的 SQL 语句
            # STRICT_TRANS_TABLES 模式要求 MySQL 在插入无效数据时抛出错误，而不是进行数据截断
            'init_command':"SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4', # 指定数据库的字符集为 utf8mb4
            'connect_timeout': 10, # 连接超时(秒)
            'read_timeout': 30, # 读取超时(秒)
            'write_timeout': 30, # 写入超时(秒)
            'ssl': {'ssl-mode': 'DISABLED'},  # 禁用 SSL 验证
        },
    }
}

# redis数据库配置
# config从.env文件中读取redis机密配置信息
REDIS_HOST = config('REDIS_HOST', default='localhost')
REDIS_PORT = config('REDIS_PORT', default=6379, cast=int)
REDIS_PASSWORD = config('REDIS_PASSWORD', default='')

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # 连接池配置
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
        }
    },
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        # "LOCATION": "redis://127.0.0.1:6379/1",
        # LOCATION:'reids://:密码@IP地址：端口号/库编号'
        "LOCATION": f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # 连接池的配置
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
        }
    },
    
    # 配置站点 短信验证码
    "sms_code": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # 连接池的配置
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
        }
    },
}

# session存储配置
# session引擎配置 -- 指定 Django 使用 缓存 (cache) 作为会话数据的存储位置，而非默认的数据库
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# 指定缓存的别名
SESSION_CACHE_ALIAS = "session"


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# 静态文件配置
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# 媒体文件配置
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

# 默认主键字段
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django REST Framework 配置
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'tools.authentication.CustomJWTAuthentication',  # 自定义 JWT 认证类
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # 默认所有API视图访问均需通过认证
    ),
}

# 配置 JWT Token 有效期和签发
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=3),  # Access Token 有效期 3 天
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),  # Refresh Token 有效期 30 天
    'ROTATE_REFRESH_TOKENS': False,  # 刷新时是否重新签发 Token -- Authing 处理
    'BLACKLIST_AFTER_ROTATION': False,  # 旧的 Refresh Token 是否失效 -- Authing 处理
    'ALGORITHM': 'RS256',  # 使用 RS256 算法
    'VERIFYING_KEY': get_jwks_client(), # 获取JWKS公钥
    'AUTH_HEADER_TYPES': ('Bearer',),
}


# 日志模块
# 日志目录
LOG_DIR = BASE_DIR.parent / 'logs'
LOG_DIR.mkdir(exist_ok=True) # 确保日志目录存在(如果不存在，则自动创建)

# 日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': str(LOG_DIR / 'django.log'),
            'formatter': 'verbose',  # 使用详细日志格式
        },
    },
    
    'formatters': {
        'verbose': {  # 详细格式
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',  # 使用 {} 样式的格式化
        },
    },
    
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',  # 记录 INFO 及以上级别日志
            'propagate': True,
        },
    },
}
