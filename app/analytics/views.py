from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from loguru import logger
from web_service.services.service_bd import get_user_hosting, get_user_domain, get_ya_user_counters
from .services.yandex_api import get_account_counters, get_visits


@login_required
def analytics(request, pk):
    domain_list = get_ya_user_counters(request)
    context = {
        'domain_list': domain_list
    }
    return render(request, 'analytics/analytics.html', context=context)


@login_required
def start_yandex_analytics(request, pk):

    # get and set yandex counters
    user_domains = get_user_domain(request)
    if get_account_counters(user_domains, pk):
        messages.success(request, 'Yandex counters successfully set')
    else:
        messages.error(request, 'Yandex counters failed set')

    # get and set visits counters
    domain_list = get_ya_user_counters(request)
    if get_visits(domain_list):
        messages.success(request, 'Yandex visits successfully set')
    else:
        messages.error(request, 'Yandex visits failed set')
    
    return redirect('analytics_urls', pk=request.user.id)

# https://api-metrika.yandex.net/management/v1/counter/67630381
# https://oauth.yandex.ru/authorize?response_type=code&client_id=c6eb276fe80b44de9bfe8a277c096ce1
# https://oauth.yandex.ru/1765411
# https://oauth.yandex.ru/authorize?grant_type=authorization_code&code=6745943&client_id=c6eb276fe80b44de9bfe8a277c096ce1
