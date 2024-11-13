from rest_framework import serializers
from .models import ChatMessage, ChatRoom

# 将 ChatMessage 模型实例序列化为 JSON 格式
class ChatMessageSerializer(serializers.ModelSerializer):
    """
    聊天消息序列化器
    """
    class Meta:
        model = ChatMessage
        fields = ['id', 'room_name', 'username', 'message', 'timestamp']

# 将 ChatRoom 模型实例序列化为 JSON 格式
class ChatRoomSerializer(serializers.ModelSerializer):
    """
    聊天房间序列化器
    """
    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'created_at']