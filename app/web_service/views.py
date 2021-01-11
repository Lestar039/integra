from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import DomainForm, HostingForm
from .models import DomainData, HostingData
from django.contrib import messages
from django.contrib.auth.models import User

from loguru import logger

from .services.service_check_status_code import check_run
from .services.service_time_comparison import domain_time_comparison, hosting_time_comparison
from .services.servece_dashboard import hosting_db, domain_db


@login_required
def save_domain(request, pk):
    """
    Save url to DB
    """
    domain_list = DomainData.objects.filter(
        username=request.user.id
    )
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = DomainForm(request.POST)
        if form.is_valid():
            domain = form.cleaned_data.get('url')
            a = form.save(commit=False)
            a.username = user
            a.save()
            form = DomainForm()
            messages.success(request, f'{domain} has been successfully added')
    else:
        form = DomainForm()

    context = {
        'form': form,
        'domains': domain_list,
    }

    return render(request, 'web_service/domain_index.html', context=context)


@login_required
def edit_domain(request, pk, url_ed):
    """
    Edit domain form
    """
    edit_form = DomainData.objects.filter(
        username=pk,
        url=url_ed
    ).first()

    if request.method == 'POST':
        form = DomainForm(request.POST, instance=edit_form)
        if form.is_valid():
            form.save()
            messages.success(request, f'{url_ed} has been updated')
            logger.debug(f'{url_ed} has been updated')
            return redirect('domains_urls', pk=request.user.id)
    else:
        form = DomainForm(instance=edit_form)
    context = {
        'form': form,
        'url': url_ed
    }
    return render(request, 'web_service/domain_edit_url.html', context=context)


@login_required
def delete_domain(request, pk, url_del):
    """
    Delete url from DB
    """
    url = DomainData.objects.get(
        username=pk,
        url=url_del)
    url.delete()
    messages.success(request, f'{url_del} has been deleted')
    return redirect('domains_urls', pk=request.user.id)


@login_required
def start_check(request):
    """
    Start parsing status code
    """
    check_run()
    messages.success(request, 'Scan websites successfully done')
    return redirect('domains_urls', pk=request.user.id)


@login_required
def save_hosting(request, pk):
    """
    Save hosting to DB
    """
    host_list = HostingData.objects.filter(
        username=request.user.id,
    )
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = HostingForm(request.POST)
        if form.is_valid():
            hosting = form.cleaned_data.get('name')
            a = form.save(commit=False)
            a.username = user
            a.save()
            form = HostingForm()
            messages.success(request, f'{hosting} has been successfully added')
    else:
        form = HostingForm()

    context = {
        'form': form,
        'hosting': host_list
    }

    return render(request, 'web_service/hosting_index.html', context=context)


@login_required
def edit_hosting(request, pk, name_ed):
    """
    Edit hosting form
    """
    edit_form = HostingData.objects.filter(
        username=pk,
        name=name_ed,
    ).first()

    if request.method == 'POST':
        form = HostingForm(request.POST, instance=edit_form)
        if form.is_valid():
            form.save()
            messages.success(request, f'{name_ed} has been updated')
            logger.debug(f'{name_ed} has been updated')
            return redirect('hosting_urls', pk=request.user.id)
    else:
        form = HostingForm(instance=edit_form)
    context = {
        'form': form,
        'host': name_ed
    }
    return render(request, 'web_service/hosting_edit_url.html', context=context)


@login_required
def delete_hosting(request, pk, name_del):
    """
    Delete hosting from DB
    """
    name = HostingData.objects.get(
        username=pk,
        name=name_del)
    name.delete()
    messages.success(request, f'{name_del} has been deleted')
    return redirect('hosting_urls', pk=request.user.id)


def redirect_to_user_page(request):
    """
    Redirect after Login to Dashboard Page
    """
    logger.debug(f'Redirect from login to {request.user.id} user dashboard')
    return redirect(f'/user/dashboard/{request.user.id}')


@login_required
def dashboard(request, pk):
    domains = domain_db(pk)
    hosting = hosting_db(pk)

    dom_ex_time = domain_time_comparison()
    host_ex_time = hosting_time_comparison()

    context = {
        'domains': domains,
        'hosting': hosting,
        'dom_ex_time': dom_ex_time,
        'host_ex_time': host_ex_time
    }

    return render(request, 'web_service/dashboard.html', context=context)
