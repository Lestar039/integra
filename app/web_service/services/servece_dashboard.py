from ..models import HostingData, DomainData
from django.contrib.auth.models import User


def domain_db(pk):
    """
    Query Set for domains
    """
    result = DomainData.objects.filter(username=pk)
    return result


def hosting_db(pk):
    """
    Query Set for hosting
    """
    result = HostingData.objects.filter(username=pk)
    return result
