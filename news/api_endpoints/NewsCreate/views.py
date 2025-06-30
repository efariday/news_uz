from rest_framework.generics import CreateAPIView
from news.models import News
from .serializers import NewsCreateSerializer

class NewsCreateAPIView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer
