from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from .serializers import *

# 服务通知详情视图
class ServiceNotificationDetail(generics.RetrieveAPIView):
    # 指定查询集为所有服务通知对象
    queryset = ServiceNotification.objects.all()
    # 指定序列化器类为服务通知序列化器
    serializer_class = ServiceNotificationSerializer

# 天气提醒详情视图
class WeatherReminderDetail(generics.RetrieveAPIView):
    queryset = WeatherReminder.objects.all()
    serializer_class = WeatherReminderSerializer

# 种植信息详情视图
class PlantingMessageDetail(generics.RetrieveAPIView):
    queryset = PlantingMessage.objects.all()
    serializer_class = PlantingMessageSerializer

# 赞评论信息详情视图
class PraiseCommentMessageDetail(generics.RetrieveAPIView):
    queryset = PraiseCommentMessage.objects.all()
    serializer_class = PraiseCommentMessageSerializer

# 系统通知详情视图
class SystemNotificationDetail(generics.RetrieveAPIView):
    queryset = SystemNotification.objects.all()
    serializer_class = SystemNotificationSerializer

# 服务通知列表视图
class ServiceNotificationList(generics.ListAPIView):
    queryset = ServiceNotification.objects.all()
    serializer_class = ServiceNotificationSerializer

# 天气提醒列表视图
class WeatherReminderList(generics.ListAPIView):
    queryset = WeatherReminder.objects.all()
    serializer_class = WeatherReminderSerializer

# 种植信息列表视图
class PlantingMessageList(generics.ListAPIView):
    queryset = PlantingMessage.objects.all()
    serializer_class = PlantingMessageSerializer

# 赞评论信息列表视图
class PraiseCommentMessageList(generics.ListAPIView):
    queryset = PraiseCommentMessage.objects.all()
    serializer_class = PraiseCommentMessageSerializer

# 系统通知列表视图
class SystemNotificationList(generics.ListAPIView):
    queryset = SystemNotification.objects.all()
    serializer_class = SystemNotificationSerializer

# 标记消息已读视图
class MarkAsReadView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        # 从请求数据中获取消息ID和类型
        message_id = request.data.get('message_id')
        message_type = request.data.get('type')

        # 根据消息类型查找对应的消息对象
        if message_type == 'service':
            message = ServiceNotification.objects.filter(id=message_id).first()
        elif message_type == 'weather':
            message = WeatherReminder.objects.filter(id=message_id).first()
        elif message_type == 'planting':
            message = PlantingMessage.objects.filter(id=message_id).first()
        elif message_type == 'like-comment':
            message = PraiseCommentMessage.objects.filter(id=message_id).first()
        elif message_type == 'system':
            message = SystemNotification.objects.filter(id=message_id).first()
        else:
            # 如果消息类型无效，则返回错误响应
            return Response({"error": "Invalid message type"}, status=status.HTTP_400_BAD_REQUEST)

        # 如果找到了消息对象，则将其状态更新为已读并保存
        if message:
            message.status = 'read'
            message.save()
            # 返回成功响应
            return Response({"status": "success", "message": "Message marked as read"}, status=status.HTTP_200_OK)
        else:
            # 如果没有找到消息对象，则返回未找到的错误响应
            return Response({"error": "Message not found"}, status=status.HTTP_404_NOT_FOUND)