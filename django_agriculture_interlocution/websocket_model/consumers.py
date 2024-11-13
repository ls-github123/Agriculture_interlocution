# 消费者
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatMessage, ChatRoom
from django.contrib.auth.models import User # 直接导入User
from django.utils import timezone
from asgiref.sync import sync_to_async
from .openai_client import OpenAiClient  # 修正类名大小写
from typing import List, Dict

MAX_MESSAGE_LENGTH = 1000

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """
        建立 WebSocket连接时调用
        """
        self.room_name = self.scope['url_route']['kwargs']['room_name']  # 从 URL 获取房间名称
        self.room_group_name = f'chat_{self.room_name}'  # 构建频道组名称
        
        # 将连接加入房间组
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()  # 接受 websocket 连接
        print(f'WebSocket连接已建立: {self.channel_name} 加入组 {self.room_group_name}')
        
    async def disconnect(self, close_code):
        """
        webSocket 断开连接时调用
        """
        # 从房间组中移除连接
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print(f'WebSocket连接已断开: {self.channel_name} 离开组 {self.room_group_name}')
        
    async def receive(self, text_data):
        """
        接收 WebSocket 消息时调用
        """
        try:
            data = json.loads(text_data)  # 解析 JSON 消息
            message = data['message']
            username = data.get('username', '匿名')
            
            if len(message) > MAX_MESSAGE_LENGTH:
                await self.send(text_data=json.dumps({
                    'message': '消息过长, 请缩短后再试。',
                    'username': '系统',
                }))
                return
            
            # 获取或创建聊天房间
            room, created = await self.get_or_create_room(self.room_name)
            
            # 获取或创建用户
            user = await self.get_user(username)
            
            # 获取对话历史
            conversation = await self.get_conversation_history(room)
            
            # 添加用户消息到对话历史
            conversation.append({"role": "user", "content": message})
            
            # 异步保存用户消息到数据库
            await self.save_message(room, user, message)
            
            # 调用大模型生成回答(流式)
            openai_client = OpenAiClient()
            async for chunk in openai_client.stream_response(conversation):
                # 将生成的内容片段发送到 websocket 客户端
                await self.send(text_data=json.dumps({
                    'message': chunk,
                    'username': '模型',  # 修正拼写错误
                }))
                # 实时保存生成的内容到数据库
                system_user = await self.get_system_user()
                await self.save_message(room, system_user, chunk)
        
        except json.JSONDecodeError:
            print("接收到的消息不是有效的 JSON 格式")
            await self.send(text_data=json.dumps({
                'message': '无效的消息格式。',
                'username': '系统',
            }))            
        
        except Exception as e:
            print(f"接收消息时发生错误: {e}")
            await self.send(text_data=json.dumps({
                'message': '处理消息时发生错误。',
                'username': '系统',
            }))
        
    async def chat_message(self, event):
        """
        处理来自房间组的消息
        """
        message = event['message']
        username = event['username']
        
        # 将消息发送到 WebSocket 客户端
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))
        
    @sync_to_async
    def save_message(self, room: ChatRoom, user: User, message: str) -> None:
        """
        将消息保存到数据库
        """
        ChatMessage.objects.create(
            room=room,
            user=user,
            message=message,
            timestamp=timezone.now()
        )
    
    @sync_to_async
    def get_conversation_history(self, room: ChatRoom) -> List[Dict[str, str]]:
        # 获取最近 20 条消息以限制上下文长度
        messages = ChatMessage.objects.filter(room=room).order_by('-timestamp')[:20]
        messages = reversed(messages)  # 按时间顺序排列
        
        conversation = []
        for msg in messages:
            role = "assistant" if msg.user.username.lower() == "模型" else "user"
            conversation.append({"role": role, "content": msg.message})
            
        return conversation
    
    @sync_to_async
    def get_or_create_room(self, room_name: str) -> tuple:
        room, created = ChatRoom.objects.get_or_create(name=room_name)
        return room, created

    @sync_to_async
    def get_user(self, username: str) -> User:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User.objects.create(username=username)
        return user

    @sync_to_async
    def get_system_user(self) -> User:
        # 获取或创建系统用户
        system_username = "模型"
        user, created = User.objects.get_or_create(username=system_username)
        return user