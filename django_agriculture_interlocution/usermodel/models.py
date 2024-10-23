from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True, verbose_name='用户ID')
    username = models.CharField(max_length=50, verbose_name='用户名')
    password = models.CharField(max_length=255, verbose_name='密码')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='邮箱')
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='电话号码')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')

    def __str__(self):
        return self.username
    

    from django.db import models

class ThirdPartyLogin(models.Model):
    id = models.AutoField(primary_key=True)  # 自增主键
    user_id = models.IntegerField()  # 用户ID
    uid = models.CharField(max_length=255)  # 第三方用户ID
    token = models.CharField(max_length=255)  # 认证令牌
    style = models.CharField(max_length=50)  # 登录方式，如：dd, weibo, wx

    def __str__(self):
        return f"ThirdPartyLogin {self.id}: {self.user_id} - {self.style}"

    class Meta:
        db_table = 'third_party_login'  # 指定数据库表名
        verbose_name = '三方登录'
        verbose_name_plural = '三方登录记录'