from rest_framework import serializers
from .models import *

# 服务通知序列化器
class ServiceNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        # 指定关联的模型
        model = ServiceNotification
        # 指定要序列化的字段，使用 '__all__' 表示所有字段
        fields = '__all__'

# 天气提醒序列化器
class WeatherReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherReminder
        fields = '__all__'

# 种植信息序列化器
class PlantingMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantingMessage
        fields = '__all__'

# 赞评论信息序列化器
class PraiseCommentMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PraiseCommentMessage
        fields = '__all__'

# 系统通知序列化器
class SystemNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemNotification
        fields = '__all__'