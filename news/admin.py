from django.contrib import admin
from news.models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "scheduled_time", "published_at")
    list_filter = ("is_published",)
    search_fields = ("title",)
