from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from .serializers import *



class ServiceNotificationDetail(generics.RetrieveAPIView):
    queryset = ServiceNotification.objects.all()
    serializer_class = ServiceNotificationSerializer

class WeatherReminderDetail(generics.RetrieveAPIView):
    queryset = WeatherReminder.objects.all()
    serializer_class = WeatherReminderSerializer

class PlantingMessageDetail(generics.RetrieveAPIView):
    queryset = PlantingMessage.objects.all()
    serializer_class = PlantingMessageSerializer

class PraiseCommentMessageDetail(generics.RetrieveAPIView):
    queryset = PraiseCommentMessage.objects.all()
    serializer_class = PraiseCommentMessageSerializer

class SystemNotificationDetail(generics.RetrieveAPIView):
    queryset = SystemNotification.objects.all()
    serializer_class = SystemNotificationSerializer










class ServiceNotificationList(generics.ListAPIView):
    queryset = ServiceNotification.objects.all()
    serializer_class = ServiceNotificationSerializer

class WeatherReminderList(generics.ListAPIView):
    queryset = WeatherReminder.objects.all()
    serializer_class = WeatherReminderSerializer

class PlantingMessageList(generics.ListAPIView):
    queryset = PlantingMessage.objects.all()
    serializer_class = PlantingMessageSerializer

class PraiseCommentMessageList(generics.ListAPIView):
    queryset = PraiseCommentMessage.objects.all()
    serializer_class = PraiseCommentMessageSerializer

class SystemNotificationList(generics.ListAPIView):
    queryset = SystemNotification.objects.all()
    serializer_class = SystemNotificationSerializer

class MarkAsReadView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        message_id = request.data.get('message_id')
        message_type = request.data.get('type')

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
            return Response({"error": "Invalid message type"}, status=status.HTTP_400_BAD_REQUEST)

        if message:
            message.status = 'read'
            message.save()
            return Response({"status": "success", "message": "Message marked as read"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Message not found"}, status=status.HTTP_404_NOT_FOUND)