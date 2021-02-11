from django.db import models


class YandexCounter(models.Model):
    domain = models.ForeignKey('web_service.DomainData', on_delete=models.CASCADE)
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
        return self.goal_number
