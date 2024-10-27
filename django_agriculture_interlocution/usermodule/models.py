from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsersManager(BaseUserManager):
    def create_user(self, user_id, username, email=None, **extra_fields):
        if not user_id:
            raise ValueError('必须提供 user_id 字段信息!')
        
        email = self.normalize_email(email) if email else None
        user = self.model(user_id=user_id, username=username, email=email, **extra_fields)
        user.set_unusable_password() # 标记用户没有本地密码
        user.save(using=self._db)
        return user
    
    def create_superuser(self, user_id, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        user = self.create_user(user_id, username, email, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user
    
# 用户信息表
class UsersModel(AbstractBaseUser, PermissionsMixin):
    # 基础用户信息
    user_id = models.CharField(max_length=255, unique=True) # 用户唯一标识付
    username = models.CharField(max_length=255, unique=True, null=True, blank=True) # 用户名--用户池内唯一
    email = models.EmailField(unique=True, null=True, blank=True) # 邮箱
    nickname = models.CharField(max_length=255, null=True, blank=True) # 昵称
    phone = models.CharField(max_length=20, null=True, blank=True) # 手机号
    phone_country_code = models.CharField(max_length=10, null=True, blank=True) # 手机区号
    
    # 账户状态信息
    status = models.CharField(max_length=50, choices=[
        ('Activated', 'Activated'),
        ('Suspended', 'Suspended'),
        ('Deactivated', 'Deactivated'),
        ('Resigned', 'Resigned'),
        ('Archived', 'Archived')
    ], default='Activated') # 账户状态
    work_status = models.CharField(max_length=50, null=True, blank=True) # 工作状态
    email_verified = models.BooleanField(default=False) # 邮箱是否验证
    phone_verified = models.BooleanField(default=False) # 手机号是否验证
    
    # 时间信息
    created_at = models.DateTimeField(null=True, blank=True) # 创建时间
    updated_at = models.DateTimeField(null=True, blank=True) # 更新时间
    last_login = models.DateTimeField(null=True, blank=True) # 上次登录时间
    
    # 用户扩展信息
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unknown')], default='U') # 性别
    address = models.CharField(max_length=255, null=True, blank=True) # 地址
    company = models.CharField(max_length=255, null=True, blank=True) # 公司
    browser = models.CharField(max_length=255, null=True, blank=True) # 最近登录的浏览器
    device = models.CharField(max_length=255, null=True, blank=True) # 最近登录的设备
    
    # 多身份源信息
    external_id = models.CharField(max_length=255, null=True, blank=True) # 外部身份源ID
    identities = models.JSONField(null=True, blank=True) # 用户身份信息(Array类型)
    
    # 权限标志
    is_active = models.BooleanField(default=True) # 是否激活
    is_staff = models.BooleanField(default=False) # 是否为管理员
    
    objects = UsersManager()
    
    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username or str(self.user_id)