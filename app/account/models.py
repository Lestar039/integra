from django.db import models
from django.conf import settings
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    telegram_id = models.BigIntegerField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.user.username

    # def get_absolute_url(self):
    #     return reverse('get_users_tickers', args=[str(self.user.id)])
