from rest_framework.generics import UpdateAPIView
from news.models import News
from .serializers import NewsUpdateSerializer

class NewsUpdateAPIView(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsUpdateSerializer
