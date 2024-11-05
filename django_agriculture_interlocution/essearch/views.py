from django.shortcuts import render
from rest_framework.views import APIView
from elasticsearch import Elasticsearch
from .models import AgricultureKnowledge
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
import warnings

# 抑制所有Elasticsearch相关的警告
warnings.filterwarnings("ignore", module="elasticsearch")

# es上传数据
es = Elasticsearch("http://20.40.103.205:9200/")

class EsAddDataView(APIView):

    permission_classes = [AllowAny] # 确保只有认证用户可以访问

    def get(self, request):
        # 农业知识库
        encyclopedias = AgricultureKnowledge.objects.all()

        for i in encyclopedias:
            es.index(index='esagriculture', body={
                'id': i.id,
                'table_name': 'esagriculture',
                'title': i.title,
                'content': i.content,
                'category': i.category,
                'author' : i.author,
                'tags' : i.tags,
            })

        return Response({'code': 200})

# es搜索数据
class EsSearch(APIView):
    permission_classes = [AllowAny] # 确保只有认证用户可以访问

    def get(self, request):
        # 获取当前页
        page = int(request.query_params.get("page", 1))
        # 每页显示多少条
        page_size = int(request.query_params.get("page_size", 4))
        # 搜索内容
        mes = request.query_params.get('mes', '')

        # 计算开始位置
        start = (page - 1) * page_size

        dsl = {
            "query": {
                "bool": {
                    "should": [
                        {"match": {"title": mes}},
                        {"match": {"content": mes}},
                        {"match": {"category": mes}},
                        {"match": {"author": mes}},
                        {"match": {"tags": mes}},
                    ]
                }
            },
            "from": start,
            "size": page_size,
            "_source": ["title", "content", "category", "author", "tags"],
        }

        # 执行搜索并获取结果
        res = es.search(index="esagriculture", body=dsl)
        data = [i["_source"] for i in res["hits"]["hits"]]

        # 计算总记录数
        total_records = res['hits']['total']['value']

        # 返回响应数据
        return Response({
            'data': data,
            'total': total_records,
            'code': 200
        })