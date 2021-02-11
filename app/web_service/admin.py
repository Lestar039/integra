from django.contrib import admin
from .models import DomainData, HostingData

# Register your models here.
admin.site.register(DomainData)
admin.site.register(HostingData)
