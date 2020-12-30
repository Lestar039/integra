from ..models import DomainData, HostingData

from datetime import datetime, timezone


def domain_time_comparison():
    """
    Create expiration time list domains
    """
    all_urls = DomainData.objects.all()
    time_now = datetime.now(timezone.utc)
    expiration_list = list()

    for _ in all_urls:
        delta = _.expiration_date - time_now
        if delta.days <= 7:
            expiration_list.append([_.url, delta.days])

    return expiration_list


def hosting_time_comparison():
    """
    Create expiration time list hosting
    """
    all_urls = HostingData.objects.all()
    time_now = datetime.now(timezone.utc)
    expiration_list = list()

    for _ in all_urls:
        delta = _.expiration_date - time_now
        if delta.days <= 7:
            expiration_list.append([_.name, delta.days])

    return expiration_list
