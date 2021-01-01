from ..models import HostingData, DomainData


def domain_db():
    """
    Query Set for domains
    """
    result = DomainData.objects.only(
        'url', 'ya_counter_number', 'expiration_date', 'status'
    )
    return result


def hosting_db():
    """
    Query Set for hosting
    """
    result = HostingData.objects.all()
    return result
