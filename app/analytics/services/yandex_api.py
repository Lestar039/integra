from web_service.models import DomainData
from .yandex_config import YA_TOKEN
from django.contrib import messages

import requests
from loguru import logger


class YandexAPI:
    """
    Create GET request
    """

    def __init__(self, url):
        self.url = url

    def parsing_data(self):

        headers = {
            'Host': 'api-metrika.yandex.net',
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {YA_TOKEN}',
        }

        try:
            response = requests.get(url=self.url, headers=headers)
            data = response.json()
            logger.debug('Got JSON from Yandex')
            return data
        except Exception as msg:
            logger.error(msg)


def create_get_request(some_url):
    """
    Using YandexAPInfo
    """
    one = YandexAPI(some_url)
    return one.parsing_data()


def get_account_counters():
    """
    Get and save all counters in current account
    """

    user_domains = DomainData.objects.all()
    account_counters_dict = {}

    try:
        get_response_from_api = create_get_request("https://api-metrika.yandex.net/management/v1/counters")
        for counter_info in range(get_response_from_api['rows']):
            for domain in user_domains:
                current_url = get_response_from_api['counters'][counter_info]['site']
                if current_url == domain.url:
                    tmp_list = list()
                    tmp_list.append(get_response_from_api['counters'][counter_info]['id'])
                    account_counters_dict[current_url] = tmp_list
                    logger.debug(f'{current_url} - OK')
        logger.debug('Yandex counters successfully set')

        logger.info(account_counters_dict)
        return account_counters_dict
    except Exception as msg:
        logger.error(msg)
        logger.error('Yandex counters failed set')


def get_any_metrics(counter_dict, any_metrics):
    """
    Get and save counter any metrics
    """

    try:
        for counter in counter_dict:
            get_metrics_counter = create_get_request(
                f"https://api-metrika.yandex.net/stat/v1/data/bytime?metrics="
                f"ym:s:{any_metrics}&date1=2daysAgo&date2=today&group=day&id={counter_dict[counter][0]}")
            metrics_value = int(get_metrics_counter['data'][0]['metrics'][0][2])
            counter_dict[counter].append(metrics_value)
        logger.debug(f'Yandex {any_metrics} successfully set')
        logger.info(f'Got {any_metrics} info')
        return counter_dict
    except Exception as msg:
        logger.error(msg)
        logger.error(f'Yandex {any_metrics} failed set')
        logger.info(counter_dict)


def get_total_goal_counter(counter_dict):
    """
    Get and save goal's: counter, name, id
    """
    try:
        for counter in counter_dict:
            counter_number = counter_dict[counter][0]
            get_goal_counters = create_get_request(
                f"https://api-metrika.yandex.net/management/v1/counter/{counter_number}/goals")
            goal_info = len(get_goal_counters['goals'])

            total_goals = 0
            for current_goal in range(goal_info):
                goal_id = get_goal_counters['goals'][current_goal]['id']
                goal_counter = _get_goal_counter(counter_number, goal_id)
                total_goals += goal_counter
            counter_dict[counter].append(total_goals)
            logger.info('Got total goal counter')
        return True
    except Exception as msg:
        logger.error(msg)
        return False


def _get_goal_counter(counter_number, goal_id):
    """
    Get goal counter
    """
    get_goal_info = create_get_request(
        f"https://api-metrika.yandex.net/stat/v1/data?id={counter_number}&metrics="
        f"ym:s:goal{goal_id}reaches&date1=today&date2=today&group=day"
    )
    return int(get_goal_info['totals'][0])


def start_yandex_api(request):

    counter_dict = get_account_counters()
    visits_dict = get_any_metrics(counter_dict, 'visits')
    hits_dict = get_any_metrics(visits_dict, 'hits')
    users_dict = get_any_metrics(hits_dict, 'users')
    get_total_goal_counter(users_dict)

    messages.success(request, 'Actual information successfully set')
    return users_dict


if __name__ == '__main__':
    pass
