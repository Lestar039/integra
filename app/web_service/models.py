from django.db import models
from django.urls import reverse
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


class YandexCounter(models.Model):
    domain = models.ForeignKey('DomainData', on_delete=models.CASCADE)
    counter_number = models.CharField(max_length=20, blank=True)
    count_visits = models.CharField(max_length=20, blank=True)
    count_hits = models.CharField(max_length=20, blank=True)
    count_views = models.CharField(max_length=20, blank=True)
    total_goals = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.counter_number


class YandexGoals(models.Model):
    counter_number = models.ForeignKey('YandexCounter', on_delete=models.CASCADE)
    goal_number = models.CharField(max_length=20)
    goal_name = models.CharField(max_length=100)
    counter_goal = models.CharField(max_length=20)

    def __str__(self):
        return self.goal_name

