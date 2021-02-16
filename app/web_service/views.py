from .forms import DomainForm, HostingForm
from .models import DomainData, HostingData

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from loguru import logger

from .services.service_check_status_code import check_run
from .services.service_time_comparison import domain_time_comparison, hosting_time_comparison, check_telegram_id


@login_required
def save_domain(request):
    """
    Save url to DB
    """
    domain_list = DomainData.objects.all()

    if request.method == 'POST':
        form = DomainForm(request.POST)
        if form.is_valid():
            domain = form.cleaned_data.get('url').lower()
            a = form.save(commit=False)
            a.url = domain
            a.save()

            check_telegram_id(request, request.user.id)
            messages.success(request, f'{domain} has been successfully added')
            form = DomainForm()
    else:
        form = DomainForm()

    context = {
        'form': form,
        'domains': domain_list,
    }

    return render(request, 'web_service/domain_index.html', context=context)


@login_required
def edit_domain(request, url_ed):
    """
    Edit domain form
    """

    edit_form = DomainData.objects.get(url=url_ed)

    if request.method == 'POST':
        form = DomainForm(request.POST, instance=edit_form)
        if form.is_valid():
            form.save()
            messages.success(request, f'{url_ed} has been updated')
            logger.debug(f'{url_ed} has been updated')
            return redirect('domains_urls')
    else:
        form = DomainForm(instance=edit_form)
    context = {
        'form': form,
        'url': url_ed
    }
    return render(request, 'web_service/domain_edit_url.html', context=context)


@login_required
def delete_domain(request, url_del):
    """
    Delete url from DB
    """

    url = DomainData.objects.get(url=url_del)
    url.delete()
    messages.success(request, f'{url_del} has been deleted')
    return redirect('domains_urls')


@login_required
def save_hosting(request):
    """
    Save hosting to DB
    """
    host_list = HostingData.objects.all()

    if request.method == 'POST':
        form = HostingForm(request.POST)
        if form.is_valid():
            hosting = form.cleaned_data.get('name')
            a = form.save(commit=False)
            a.save()

            check_telegram_id(request, request.user.id)
            messages.success(request, f'{hosting} has been successfully added')
            form = HostingForm()
    else:
        form = HostingForm()

    context = {
        'form': form,
        'hosting': host_list
    }

    return render(request, 'web_service/hosting_index.html', context=context)


@login_required
def edit_hosting(request, name_ed):
    """
    Edit hosting form
    """
    edit_form = HostingData.objects.get(name=name_ed)

    if request.method == 'POST':
        form = HostingForm(request.POST, instance=edit_form)
        if form.is_valid():
            form.save()
            messages.success(request, f'{name_ed} has been updated')
            logger.debug(f'{name_ed} has been updated')
            return redirect('hosting_urls')
    else:
        form = HostingForm(instance=edit_form)
    context = {
        'form': form,
        'host': name_ed
    }
    return render(request, 'web_service/hosting_edit_url.html', context=context)


@login_required
def delete_hosting(request, name_del):
    """
    Delete hosting from DB
    """
    name = HostingData.objects.get(name=name_del)
    name.delete()
    messages.success(request, f'{name_del} has been deleted')
    return redirect('hosting_urls')


def redirect_to_user_page(request):
    """
    Redirect after Login to Dashboard Page
    """
    logger.debug(f'Redirect from login to {request.user.id} user dashboard')
    return redirect(f'/user/dashboard/')


@login_required
def start_check(request):
    """
    Start parsing status code
    """
    check_run()
    messages.success(request, 'Scan websites successfully done')
    return redirect('domains_urls')


@login_required
def dashboard(request):
    """
    All-in-one page information
    """
    domains = DomainData.objects.all()
    hosting = HostingData.objects.all()

    dom_ex_time = domain_time_comparison(request)
    host_ex_time = hosting_time_comparison(request)

    context = {
        'domains': domains,
        'hosting': hosting,
        'dom_ex_time': dom_ex_time,
        'host_ex_time': host_ex_time
    }

    return render(request, 'web_service/dashboard.html', context=context)
