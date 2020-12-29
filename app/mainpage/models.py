from django.db import models
from django.urls import reverse


class WebsiteData(models.Model):
    url = models.CharField(max_length=100, primary_key=True, verbose_name='URL')
    status = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.url

    def get_absolute_url(self):
        return reverse('save_urls')
