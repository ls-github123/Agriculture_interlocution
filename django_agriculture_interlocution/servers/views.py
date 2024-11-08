from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from servers.MyAI.issue import issue
import logging
import json
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import FormParser,JSONParser
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
            logger.info(f"Received issue_info: {issue_info}")
            print(issue_info)

            # 尝试获取 species 参数
            species = issue_info.get('species')
            print(f'打印{species}')
            print(type(species))

            if not species:
                return Response({'error': '缺少必要的参数: species', 'code': 400}, status=400)

            # 构建 species_dict
            species_dict = {'species': species}
            print(f'转换后的字典: {species_dict}')
            print(type(species_dict))

            # 调用 AI 生成回答
            ai_message = issue(species_dict)
            logger.info(f"Generated AI message: {ai_message}")
            print(ai_message)

            return Response({'aiMessage': ai_message, 'code': 200})

        except json.JSONDecodeError as e:
            logger.error(f"JSON Decode Error: {e}")
            return Response({'error': f'JSON Decode Error: {e}', 'code': 400}, status=400)

        except KeyError as e:
            logger.error(f"KeyError occurred: {e}")
            return Response({'error': f'KeyError: {e}', 'code': 400}, status=400)

        except Exception as e:
            logger.error(f"An error occurred: {e}")
            return Response({'error': str(e), 'code': 500}, status=500)
        