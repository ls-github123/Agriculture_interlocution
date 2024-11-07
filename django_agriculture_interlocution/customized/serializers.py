from rest_framework import serializers
from .models import HarvestRequest,IrrigationRequest

class HarvestRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HarvestRequest
        fields = ['id', 'name', 'phone', 'address', 'crop_type']

class IrrigationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = IrrigationRequest
        fields = ['id', 'name', 'phone', 'address', 'crop_type', 'irrigation_type']