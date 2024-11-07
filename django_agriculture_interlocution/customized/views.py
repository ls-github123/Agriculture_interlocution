from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HarvestRequestSerializer,IrrigationRequestSerializer
from .models import HarvestRequest

class HarvestRequestView(APIView):
    permission_classes = [AllowAny]#身份信息验证
    def post(self, request):
        serializer = HarvestRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class IrrigationRequestView(APIView):
    permission_classes = [AllowAny]#身份信息验证
    def post(self, request):
        serializer = IrrigationRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

