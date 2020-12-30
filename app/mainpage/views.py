from django.shortcuts import render, redirect
from .forms import WebsiteForm
from .models import WebsiteData
from django.views.generic import TemplateView
from django.contrib import messages

from .services.service_check_status_code import check_run


def save_url(request):
    """
    Save url to DB
    """
    site_list = WebsiteData.objects.all()

    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            form.save()
            form = WebsiteForm()
            messages.success(request, 'URL has been successfully added')
    else:
        form = WebsiteForm()

    context = {
        'form': form,
        'sites': site_list
    }

    return render(request, 'mainpage/index.html', context=context)


def delete_url(request, url_del):
    """
    Delete url from DB
    """
    url = WebsiteData.objects.get(url=url_del)
    url.delete()
    messages.success(request, 'URL has been deleted')
    return redirect('save_urls')


def start_check(request):
    """
    Start parsing status code
    """
    check_run()
    messages.success(request, 'Scan websites successfully done')
    return redirect('save_urls')


class AnalyticsView(TemplateView):
    template_name = 'mainpage/analytics.html'


class CalendarView(TemplateView):
    template_name = 'mainpage/calendar.html'
