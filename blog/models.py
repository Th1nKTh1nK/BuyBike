from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Ad(models.Model):
    ad_price = models.TextField()
    ad_category = models.TextField()
    ad_title = models.TextField()
    ad_id = models.TextField()
    ad_id_link = models.TextField()
    ad_image = models.TextField()

    def __str__(self):
        return self.ad_title
