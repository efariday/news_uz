from rest_framework.generics import RetrieveAPIView
from news.models import News
from .serializers import NewsDetailSerializer

class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
