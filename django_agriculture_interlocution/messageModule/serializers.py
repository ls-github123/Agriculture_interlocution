from rest_framework import serializers
from .models import *













class ServiceNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceNotification
        fields = '__all__'

class WeatherReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherReminder
        fields = '__all__'

class PlantingMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantingMessage
        fields = '__all__'

class PraiseCommentMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PraiseCommentMessage
        fields = '__all__'

class SystemNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemNotification
        fields = '__all__'