from rest_framework import serializers
from news.models import News

class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
