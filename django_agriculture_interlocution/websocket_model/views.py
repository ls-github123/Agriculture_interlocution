from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import ChatMessage, ChatRoom
from .serializers import ChatMessageSerializer, ChatRoomSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class ChatHistoryView(APIView):
    """
    获取指定房间的聊天历史记录
    """
    permission_classes = [IsAuthenticated] # 仅允许已认证用户访问
    
    def get(self, request, room_name, format=None):
        """
        获取指定房间的最近50条消息
        """
        messages = ChatMessage.objects.filter(room_name=room_name).order_by('-timestamp')[:50]
        serializer = ChatMessageSerializer(messages, many=True)
        return Response (serializer.data, status=status.HTTP_200_OK)

class ChatRoomListCreateView(APIView):
    """
    获取所有聊天房间或创建新的聊天房间
    """
    permission_classes = [IsAuthenticated] # 仅允许已认证用户访问
    
    def get(self, request, format=None):
        rooms = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        """
        创建一个新的聊天房间
        """
        serializer = ChatRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)