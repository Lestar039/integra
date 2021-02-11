from ..models import YandexCounter


def get_ya_user_counters(request):
    """
    Get user's counters
    """
    users_counters_list = YandexCounter.objects.filter(domain__username=request.user.id)
    return users_counters_list
