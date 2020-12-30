from django.shortcuts import render, redirect
from .forms import WebsiteForm
from .models import WebsiteData
from django.views.generic import TemplateView
from django.contrib import messages

from loguru import logger

from .services.service_check_status_code import check_run
from .services.service_time_comparison import time_comparison


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

    time_ex = time_comparison()

    context = {
        'form': form,
        'sites': site_list,
        'time': time_ex
    }

    return render(request, 'mainpage/index.html', context=context)


def edit_url(request, url_ed):
    """
    Edit ticker form user account
    """
    edit_form = WebsiteData.objects.filter(
        url=url_ed,
    ).first()

    if request.method == 'POST':
        form = WebsiteForm(request.POST, instance=edit_form)
        if form.is_valid():
            form.save()
            messages.success(request, f'{url_ed} has been updated')
            logger.debug(f'{url_ed} has been updated')
            return redirect('save_urls')
    else:
        form = WebsiteForm(instance=edit_form)
    context = {
        'form': form,
        'url': url_ed
    }
    return render(request, 'mainpage/edit_url.html', context=context)


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
