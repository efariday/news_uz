from rest_framework.generics import ListAPIView
from news.models import News
from .serializers import NewsListSerializer

class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
