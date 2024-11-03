from rest_framework import serializers
from .models import AgricultureKnowledge

class AgricultureKnowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgricultureKnowledge
        fields = ['id', 'title', 'content', 'category', 'author', 'tags', 'date']