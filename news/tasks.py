from celery import shared_task
from django.utils import timezone
from news.models import News

@shared_task
def publish_scheduled_news():
    now = timezone.now()
    News.objects.filter(is_published=False, scheduled_time__lte=now).update(
        is_published=True,
        published_at=now
    )
