from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel  # created_at, updated_at bo'lsa

class News(BaseModel):
    title = models.CharField(_("Title"), max_length=255)
    body = models.TextField(_("Body"))
    image = models.ImageField(_("Image"), upload_to="news/", null=True, blank=True)
    is_published = models.BooleanField(_("Is Published"), default=False)
    published_at = models.DateTimeField(_("Publish Time"), null=True, blank=True)
    scheduled_time = models.DateTimeField(_("Scheduled Time"), null=True, blank=True)


    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")

    def __str__(self):
        return self.title
