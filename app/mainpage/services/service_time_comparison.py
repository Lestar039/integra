from ..models import WebsiteData

from datetime import datetime, timezone


def time_comparison():
    """
    Create expiration time list websites
    """
    all_urls = WebsiteData.objects.all()
    time_now = datetime.now(timezone.utc)
    expiration_list = list()

    for _ in all_urls:
        delta = _.expiration_date - time_now
        if delta.days <= 7:
            expiration_list.append([_.url, delta.days])

    return expiration_list
