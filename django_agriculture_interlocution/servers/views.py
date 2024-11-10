from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from servers.MyAI.issue import issue
import logging
import json
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import FormParser,JSONParser
import requests
# Create your views here.
# 配置日志记录
logger = logging.getLogger(__name__)
# 请求

class IssueView(APIView):

    permission_classes = [AllowAny] # 确保只有认证用户可以访问
    parser_classes=[FormParser,JSONParser] #支持JSON和表单数据
    def post(self, request):
        try:
            # 获取请求数据
            issue_info = request.data
            
            logger.info(f"Received issue_info: {issue_info}")#日志
            print(f'输出{issue_info}')
            print(type(issue_info))

            # 尝试获取 species 参数
            species = issue_info.get('species')
            print(f'打印{species}')
            print(type(species))

            if not species:
                return JsonResponse({'error': '缺少必要的参数: species', 'code': 400}, status=400)

            

            # 调用 AI 大模型生成回答
            ai_message = self.generate_ai_response(species)
            logger.info(f"Generated AI message: {ai_message}")#日志
            print(f'ai_message:{ai_message}')

            return JsonResponse({'aiMessage': ai_message, 'code': 200})

        except Exception as e:
            logger.error(f"JSON Decode Error: {e}")#日志
            return JsonResponse({'error': str(e), 'code': 500}, status=500)

    def generate_ai_response(self,species):
        # 这里调用大模型生成回答
        prompt=f"我的问题是关于{species}，请帮我提几个建议"
        api_key = 'sk-7120502d21944e6db08732969adae8a6',# 实际的 API 密钥
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        url='https://dashscope.aliyuncs.com/compatible-mode/v1/',#替换为实际的大模型API地址
        try:
            response = requests.post(url, json={'prompt': prompt}, headers=headers)
            logger.info(f"API Response Status Code: {response.status_code}")
            logger.info(f"API Response Content: {response.content}")

            if response.status_code == 200:
                return response.json().get('response', '生成失败')
            else:
                error_message = response.json().get('error', '未知错误')
                logger.error(f"API Error: {error_message}")
                return f'生成失败: {error_message}'
        except requests.RequestException as e:
            logger.error(f"Request Exception: {e}")
            return '生成失败，请稍后再试'