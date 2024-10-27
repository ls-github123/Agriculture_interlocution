from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    """
    用户表
    """
    user_id = models.AutoField(primary_key=True, verbose_name='用户ID')
    username = models.CharField(max_length=50, verbose_name='用户名')
    password = models.CharField(max_length=255, verbose_name='密码')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='邮箱')
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='电话号码')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')

    def __str__(self):
        return self.username
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

class MessageType(models.Model):
    """
    消息类型表
    """
    type_id = models.AutoField(primary_key=True, verbose_name='类型ID')
    type_name = models.CharField(max_length=50, verbose_name='类型名称')
    icon_url = models.URLField(max_length=200, null=True, blank=True, verbose_name='图标URL')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='创建时间')

    def __str__(self):
        return self.type_name
    class Meta:
        verbose_name = '消息类型'
        verbose_name_plural = '消息类型'

class Message(models.Model):
    """
    消息表
    """
    class StatusChoices(models.TextChoices):
        UNREAD = 'unread', '未读'
        READ = 'read', '已读'
        DELETED = 'deleted', '已删除'

    class PriorityChoices(models.TextChoices):
        LOW = 'low', '低'
        MEDIUM = 'medium', '中'
        HIGH = 'high', '高'

    message_id = models.AutoField(primary_key=True, verbose_name='消息ID')
    type_id = models.ForeignKey(MessageType, on_delete=models.CASCADE,db_column='type_id',verbose_name='类型ID')
    title = models.CharField(max_length=100, verbose_name='消息标题')
    content = models.TextField(verbose_name='消息内容')
    sender_id = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE, db_column='sender_id',verbose_name='发送者ID')
    receiver_id = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE, db_column='receiver_id',verbose_name='接收者ID')
    send_time = models.DateTimeField(auto_now_add=True, verbose_name='发送时间')
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.UNREAD, verbose_name='消息状态')
    priority = models.CharField(max_length=20, choices=PriorityChoices.choices, default=PriorityChoices.MEDIUM, verbose_name='优先级')
    read_time = models.DateTimeField(null=True, blank=True, verbose_name='阅读时间')
    attachments = models.JSONField(null=True, blank=True, verbose_name='附件')
    category = models.CharField(max_length=50, null=True, blank=True, verbose_name='消息分类')
    tags = models.CharField(max_length=200, null=True, blank=True, verbose_name='标签')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '消息'
        verbose_name_plural = '消息'
    

class Feedback(models.Model):
    """
    反馈表
    """
    feedback_id = models.AutoField(primary_key=True, verbose_name='反馈ID')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,db_column='user_id', verbose_name='用户ID')
    description = models.TextField(max_length=1000, verbose_name='反馈描述')
    problem_type = models.CharField(max_length=50, choices=[
        ('功能建议', '功能建议'),
        ('页面问题', '页面问题'),
        ('操作问题', '操作问题'),
        ('功能问题', '功能问题'),
        ('购买问题', '购买问题'),
        ('其他', '其他')
    ], verbose_name='问题类型')
    contact_person = models.CharField(max_length=50, verbose_name='联系人')
    contact_phone = models.CharField(max_length=20, verbose_name='联系电话')
    attachment_urls = models.JSONField(default=list, verbose_name='附件URL数组')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return f"{self.user_id} - {self.problem_type}"
    class Meta:
        verbose_name = '反馈'
        verbose_name_plural = '反馈'