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