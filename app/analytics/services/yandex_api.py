from web_service.models import DomainData, YandexCounter
from web_service.services.service_bd import get_user_domain, get_user, get_ya_user_counters

try:
    from yandex_config import YA_TOKEN
except ImportError:
    from .yandex_config import YA_TOKEN

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


def get_account_counters(user_domains, pk):
    """
    Get all counters in current account
    """
    one = YandexAPInfo()
    user = get_user(pk)
    ya_counters = one.parsing_data_from_yandex_api(f"https://api-metrika.yandex.net/management/v1/counters")

    try:
        for _ in range(ya_counters['rows']):
            for i in user_domains:
                domain = ya_counters['counters'][_]['site']
                if domain == i.url:
                    a = DomainData.objects.filter(username=user, url=domain).first()
                    YandexCounter.objects.update_or_create(
                        domain=a, defaults={'counter_number': ya_counters['counters'][_]['id']}
                    )
                    logger.debug(domain, i.url)
        return True
    except Exception as msg:
        logger.error(msg)
        return False


def get_visits(counter_list):
    """
    Total count visits
    """
    one = YandexAPInfo()
    logger.debug(counter_list)

    try:
        for _ in counter_list:
            counter_visits = one.parsing_data_from_yandex_api(
                f"https://api-metrika.yandex.net/stat/v1/data/bytime?metrics="
                f"ym:s:visits&date1=2daysAgo&date2=today&group=day&id={_.counter_number}")

            YandexCounter.objects.update_or_create(
                counter_number=_.counter_number, defaults={'count_visits': counter_visits['data'][0]['metrics'][0][2]}
            )
            logger.debug(_.counter_number)
        return True
    except Exception as msg:
        logger.error(msg)
        return False


def start_yandex_api():
    # 1. Yandex counter number
    get_account_counters(user_domains, pk)

    # 2. Today_visits
    get_visits(counters_list_of_list)


if __name__ == '__main__':
    start_yandex_api()
