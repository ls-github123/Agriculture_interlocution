from rest_framework import serializers
from .models import HarvestRequest

class HarvestRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HarvestRequest
        fields = ['id', 'name', 'phone', 'address', 'crop_type']