from django.shortcuts import render
from django.views.generic import TemplateView

from .services.service_check_status_code import check_run


class IndexPageView(TemplateView):
    template_name = 'mainpage/index.html'


def index_page(request):
    site_list = check_run()
    return render(request, 'mainpage/index.html', context={'sites': site_list})


class AnalyticsView(TemplateView):
    template_name = 'mainpage/analytics.html'


class CalendarView(TemplateView):
    template_name = 'mainpage/calendar.html'
