from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsersManager(BaseUserManager):
    """
    自定义用户管理器, 创建普通用户和超级用户。
    主要负责用户创建的逻辑。
    """
    # 创建并保存用户
    def create_user(self, sub, phone_number, password=None, **extra_fields):
        if not sub:
            raise ValueError('用户必须有一个唯一标识符(sub)!')
        if not phone_number:
            raise ValueError('用户必须有手机号')
        
        user = self.model(sub=sub, phone_number=phone_number, **extra_fields)
        user.set_unusable_password() # 不设置密码
        user.save(using=self._db) # # 保存用户到数据库
        return user
    
    # 创建并保存一个超级用户,具有管理权限
    def create_superuser(self, sub, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(sub, phone_number, password, **extra_fields)
    
class UsersModel(AbstractBaseUser, PermissionsMixin):
    sub = models.CharField(max_length=255, unique=True, primary_key=True)
    phone_number = models.CharField(max_length=20, unique=True)
    phone_number_verified = models.BooleanField(default=False)
    email = models.EmailField(unique=True, null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False) # 用户是否实名认证
    
    # 使用自定义的用户管理器
    objects = UsersManager()
    
    # 认证系统所需字段: 指定用于登录的字段
    USERNAME_FIELD = 'sub'
    REQUIRED_FIELDS = ['phone_number']
    
    class Meta:
        db_table = 'auth_user'
        verbose_name = '用户'
        verbose_name_plural = '用户'
        
    def __str__(self):
        return self.sub # 返回用户的唯一标识符
    
class UserProfile(models.Model):
    """
    用户扩展资料模型, 与UsersModel 形成一对一关系, 存储用户详细资料
    """
    user = models.OneToOneField(UsersModel, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=150, null=True, blank=True)
    given_name = models.CharField(max_length=150, null=True, blank=True)
    middle_name = models.CharField(max_length=150, null=True, blank=True)
    family_name = models.CharField(max_length=150, null=True, blank=True)
    nickname = models.CharField(max_length=150, null=True, blank=True)
    preferred_username = models.CharField(max_length=150, null=True, blank=True)
    profile = models.URLField(null=True, blank=True)
    picture = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=1,
        choices=[('M', '男性'), ('F', '女性'), ('O', '其他')],
        null=True,
        blank=True
    )
    zoneinfo = models.CharField(max_length=50, null=True, blank=True)
    locale = models.CharField(max_length=50, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'user_profile'
        verbose_name = '用户资料'
        verbose_name_plural = '用户资料'
    
    def __str__(self):
        return f"{self.user.sub} 的资料" # # 返回用户的唯一标识符及资料说明
    
class UserVerification(models.Model):
    """
    用户实名认证模型, 与UserModel 形成一对一关系, 存储用户实名信息。
    """
    user = models.OneToOneField(UsersModel, on_delete=models.CASCADE, related_name='verification')
    real_name = models.CharField(max_length=20) # 用户真实姓名
    id_card_number = models.CharField(max_length=18, unique=True) # 用户身份证号, 唯一
    verified_at = models.DateTimeField(auto_now_add=True) # 认证时间，自动创建
    
    class Meta:
        db_table = 'user_verification'
        verbose_name = '用户实名认证'
        verbose_name_plural = '用户实名认证'
        
    def __str__(self):
        return f"{self.user.sub} 的实名认证信息" # 返回用户的唯一标识符及实名认证信息