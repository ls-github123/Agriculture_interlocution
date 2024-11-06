from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from servers.MyAI.issue import issue
import logging
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import JSONParser
# Create your views here.
# 配置日志记录
logger = logging.getLogger(__name__)
# 请求
class IssueView(APIView):

    permission_classes = [AllowAny] # 确保只有认证用户可以访问
    parser_classes=[JSONParser]
    def post(self, request):
        # 获取请求数据
        logger.info(f"Received request data: {request.data}")

        # 尝试获取 species 参数
        species = request.data.get('species')
        if not species:
            return Response({'error': '缺少必要的参数: species', 'code': 400}, status=400)

        logger.info(f"Extracted species: {species}")

        # 调用 AI 生成回答
        ai_message = issue(species)
        logger.info(f"Generated AI message: {ai_message}")
        return Response({'aiMessage': ai_message, 'code': 200})