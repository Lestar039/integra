from django.db import models
from django.urls import reverse


class HostingData(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    account = models.CharField(max_length=100)
    expiration_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name


class DomainData(models.Model):
    url = models.CharField(max_length=100, primary_key=True)
    ya_counter_number = models.CharField(max_length=20, blank=True)
    expiration_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=20, blank=True)
    hosting = models.ForeignKey(HostingData, on_delete=models.CASCADE)

    def __str__(self):
        return self.url

    def get_absolute_url(self):
        return reverse('save_urls')
