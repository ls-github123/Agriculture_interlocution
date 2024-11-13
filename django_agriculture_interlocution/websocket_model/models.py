from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatRoom(models.Model):
    """
    聊天房间模型
    """
    room_name = models.CharField(max_length=255, unique=True)  # 房间名称，唯一
    created_at = models.DateTimeField(auto_now_add=True)  # 房间创建时间

    def __str__(self):
        return self.room_name

class ChatMessage(models.Model):
    """
    聊天消息模型
    """
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')  # 关联的聊天房间
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')       # 发送者用户
    message = models.TextField()  # 消息内容
    timestamp = models.DateTimeField(auto_now_add=True)  # 消息发送时间

    class Meta:
        indexes = [
            models.Index(fields=['room', 'timestamp']),
        ]
        ordering = ['timestamp']  # 默认按时间排序

    def __str__(self):
        return f'[{self.timestamp}] {self.user.username}: {self.message}'