from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'phone_number']

class MessageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageType
        fields = ['type_id', 'type_name', 'icon_url']

class MessageSerializer(serializers.ModelSerializer):
    type_id = MessageTypeSerializer(read_only=True)
    sender_id = UserSerializer(read_only=True)
    receiver_id = UserSerializer(read_only=True)
    send_time_formatted = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = [
            'message_id', 'type_id', 'title', 'content', 'sender_id', 'receiver_id',
            'send_time', 'send_time_formatted', 'status', 'priority', 'read_time', 'attachments', 'category', 'tags'
        ]

    def get_send_time_formatted(self, obj):
        return obj.send_time.strftime('%Y-%m-%d %H:%M:%S')