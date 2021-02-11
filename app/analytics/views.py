from .models import YandexCounter
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .services.yandex_api import start_yandex_api


@login_required
def analytics(request):
    domain_list = YandexCounter.objects.all()
    context = {
        'domain_list': domain_list
    }
    return render(request, 'analytics/analytics.html', context=context)


@login_required
def start_yandex_analytics(request):
    start_yandex_api(request)
    return redirect('analytics_urls')
