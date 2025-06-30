from django.urls import path
from news.api_endpoints import (
    NewsListAPIView,
    NewsCreateAPIView,
    NewsDetailAPIView,
    NewsUpdateAPIView,
    NewsDeleteAPIView,
)

urlpatterns = [
    path('', NewsListAPIView.as_view(), name='news-list'),
    path('create/', NewsCreateAPIView.as_view(), name='news-create'),
    path('<int:pk>/', NewsDetailAPIView.as_view(), name='news-detail'),
    path('<int:pk>/update/', NewsUpdateAPIView.as_view(), name='news-update'),
    path('<int:pk>/delete/', NewsDeleteAPIView.as_view(), name='news-delete'),
]
