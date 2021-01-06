from django.shortcuts import render


def analytics(request, pk):
    return render(request, 'analytics/analytics.html')


# https://api-metrika.yandex.net/management/v1/counter/67630381
# https://oauth.yandex.ru/authorize?response_type=code&client_id=c6eb276fe80b44de9bfe8a277c096ce1
# https://oauth.yandex.ru/1765411
# https://oauth.yandex.ru/authorize?grant_type=authorization_code&code=6745943&client_id=c6eb276fe80b44de9bfe8a277c096ce1
