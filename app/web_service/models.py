from django.db import models
from django.conf import settings


class HostingData(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, primary_key=True)
    account = models.CharField(max_length=100)
    expiration_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name


class DomainData(models.Model):
    hosting = models.ForeignKey(HostingData, on_delete=models.CASCADE)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    url = models.CharField(max_length=100, primary_key=True)
    expiration_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=20, blank=True)
    ssh = models.BooleanField(default=False)

    def __str__(self):
        return self.url
