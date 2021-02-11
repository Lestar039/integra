from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .services.service_bd import get_ya_user_counters
from .services.yandex_api import start_yandex_api


@login_required
def analytics(request, pk):
    domain_list = get_ya_user_counters(request)
    context = {
        'domain_list': domain_list
    }
    return render(request, 'analytics/analytics.html', context=context)


@login_required
def start_yandex_analytics(request, pk):
    start_yandex_api(request, pk)
    return redirect('analytics_urls', pk=request.user.id)
