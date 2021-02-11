from web_service.models import DomainData
from ..models import YandexCounter, YandexGoals
from web_service.services.service_bd import get_user_domain, get_user
from .service_bd import get_ya_user_counters
from .yandex_config import YA_TOKEN
from django.contrib import messages

import requests
from loguru import logger


class YandexAPInfo:

    def parsing_data_from_yandex_api(self, url):
        """
        Create GET request
        """

        headers = {
            'Host': 'api-metrika.yandex.net',
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {YA_TOKEN}',
        }

        try:
            response = requests.get(url=url, headers=headers)
            data = response.json()
            # logger.debug(data)
            return data
        except Exception as msg:
            logger.error(msg)


def get_account_counters(user_domains):
    """
    Get all counters in current account
    """
    one = YandexAPInfo()
    ya_counters = one.parsing_data_from_yandex_api(f"https://api-metrika.yandex.net/management/v1/counters")

    try:
        for _ in range(ya_counters['rows']):
            for i in user_domains:
                domain = ya_counters['counters'][_]['site']
                if domain == i.url:
                    a = DomainData.objects.get(url=domain)
                    YandexCounter.objects.update_or_create(
                        domain=a, defaults={'counter_number': ya_counters['counters'][_]['id']}
                    )
                    # logger.debug(domain, i.url)
        return True
    except Exception as msg:
        logger.error(msg)
        return False


def get_any_counters(counter_list, ya_metrics, counter_name):
    """
    Total count something
    """
    one = YandexAPInfo()

    try:
        for _ in counter_list:
            counter = one.parsing_data_from_yandex_api(
                f"https://api-metrika.yandex.net/stat/v1/data/bytime?metrics="
                f"ym:s:{ya_metrics}&date1=2daysAgo&date2=today&group=day&id={_.counter_number}")

            YandexCounter.objects.update_or_create(
                counter_number=_.counter_number, defaults={counter_name: int(counter['data'][0]['metrics'][0][2])}
            )
            # logger.debug(_.counter_number)
        return True
    except Exception as msg:
        logger.error(msg)
        return False


def get_goal_numbers(counter_list):
    """
    Get and goal info and save: counter, name, id
    """
    one = YandexAPInfo()

    try:
        for _ in counter_list:
            goal_counters = one.parsing_data_from_yandex_api(
                f"https://api-metrika.yandex.net/management/v1/counter/{_.counter_number}/goals")
            goal_info = len(goal_counters['goals'])

            for i in range(goal_info):
                goal_name = goal_counters['goals'][i]['name']
                goal_id = goal_counters['goals'][i]['id']
                logger.debug(goal_id)

                _save_goal_name_id(_.counter_number, goal_id, goal_name)
                _get_goal_counter(_.counter_number, goal_id)
                _total_goals(_.counter_number)

        return True
    except Exception as msg:
        logger.error(msg)
        return False


def _save_goal_name_id(counter_number, goal_id, goal_name):
    try:
        goal_counter = YandexGoals.objects.filter(goal_number=goal_id, goal_name=goal_name).first()
        logger.debug(f"Goal '{goal_counter}' has already been created")
    except Exception as msg:
        current_yandex_counter = YandexCounter.objects.filter(counter_number=counter_number).first()
        goal_counter = YandexGoals.objects.create(
            counter_number=current_yandex_counter, goal_number=goal_id, goal_name=goal_name
        )
        logger.debug(msg)
        logger.debug(f"Goal '{goal_counter}' successfully set")


def _get_goal_counter(counter_number, goal_number):
    """
    Get and save goal counter
    """
    counter = YandexCounter.objects.get(counter_number=counter_number)

    one = YandexAPInfo()
    get_goal_info = one.parsing_data_from_yandex_api(
        f"https://api-metrika.yandex.net/stat/v1/data?id={counter_number}&metrics="
        f"ym:s:goal{goal_number}reaches&date1=today&date2=today&group=day"
    )
    counter_goal = get_goal_info['totals'][0]
    # logger.debug(get_goal_info)
    try:
        YandexGoals.objects.update_or_create(
            goal_number=goal_number, counter_number=counter,
            defaults={"counter_goal": counter_goal}
        )
        logger.debug(f"Total goal counter '{counter_goal}' successfully save")
    except Exception as msg:
        logger.error(msg)


def _total_goals(counter_number):
    """
    Get total goal counter
    """
    counter = YandexCounter.objects.get(counter_number=counter_number)
    all_goal = YandexGoals.objects.filter(
        counter_number=counter
    )
    # logger.debug(all_goal)
    counter = 0
    for _ in all_goal:
        counter += float(_.counter_goal)

    # logger.debug(counter)

    YandexCounter.objects.update_or_create(
        counter_number=counter_number, defaults={
            "total_goals": int(counter)}
    )


def start_yandex_api(request):
    try:
        user_domains = DomainData.objects.all()

        if get_account_counters(user_domains):
            logger.debug('Yandex counters successfully set')
        else:
            logger.error('Yandex counters failed set')

        domain_list = YandexCounter.objects.all()

        if get_any_counters(domain_list, 'visits', 'count_visits'):
            logger.debug('Yandex visits successfully set')
        else:
            logger.error('Yandex visits failed set')

        if get_any_counters(domain_list, 'hits', 'count_hits'):
            logger.debug('Yandex hits successfully set')
        else:
            logger.error('Yandex hits failed set')

        if get_any_counters(domain_list, 'users', 'count_views'):
            logger.debug('Yandex views successfully set')
        else:
            logger.error('Yandex views failed set')

        if get_goal_numbers(domain_list):
            logger.debug('Yandex goals successfully set')
        else:
            logger.error('Yandex goals failed set')

        messages.success(request, 'Actual information successfully set')

    except Exception as msg:
        messages.error(request, msg)


if __name__ == '__main__':
    pass
