from django.contrib.auth.models import User

from ..models import HostingData, DomainData


def get_user_hosting(request):
    """
    Get user's hosting
    """
    hosting_list = HostingData.objects.filter(
        username=request.user.id
    )
    return hosting_list


def get_user_domain(request):
    """
        Get user's domain
    """
    domain_list = DomainData.objects.filter(
        username=request.user.id
    )
    return domain_list


def get_user(pk):
    """
    Get current user
    """
    user = User.objects.get(id=pk)
    return user
