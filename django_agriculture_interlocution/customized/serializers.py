from rest_framework import serializers
from .models import HarvestRequest,IrrigationRequest,Crop

class HarvestRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HarvestRequest
        fields = ['id', 'name', 'phone', 'address', 'cropType']

class IrrigationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = IrrigationRequest
        fields = ['id', 'name', 'phone', 'address', 'crop_type', 'irrigation_type']


class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = ['id', 'name', 'plantingdate']
