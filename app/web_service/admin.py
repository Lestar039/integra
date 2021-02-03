from django.contrib import admin
from .models import DomainData, HostingData, YandexCounter, YandexGoals

# Register your models here.
admin.site.register(DomainData)
admin.site.register(HostingData)
admin.site.register(YandexCounter)
admin.site.register(YandexGoals)
