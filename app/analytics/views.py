from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .services.yandex_api import start_yandex_api


@login_required
def analytics(request):
    data = start_yandex_api(request)

    context = {
        'data': data
    }
    return render(request, 'analytics/analytics.html', context=context)
