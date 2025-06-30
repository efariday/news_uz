from rest_framework.generics import DestroyAPIView
from news.models import News
from .serializers import NewsDeleteSerializer

class NewsDeleteAPIView(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDeleteSerializer
