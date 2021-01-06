import requests
from app.integra.local_settings import YA_TOKEN
from loguru import logger


class YandexAPInfo:

    def __init__(self, counter_number):
        self.counter_number = counter_number

    def get_info(self, end_url):
        """
        Create GET request
        """
        # The counter
        # url = f"https://api-metrika.yandex.net/management/v1/counter/{self.counter_number}"
        # logger.info(url)
        # All Account Counters
        # url = f"https://api-metrika.yandex.net/management/v1/counters"

        # Total visits >>>>>>>>>>>>>>>
        # url = f"https://api-metrika.yandex.net/stat/v1/data?metrics=ym:s:visits&id={self.counter_number}"
        # Total hits >>>>>>>>>>>>>>>>>>>>>>>>>
        # url = f"https://api-metrika.yandex.net/stat/v1/data?metrics=ym:s:hits&id={self.counter_number}"
        # Total goal >>>>>>>>>>>>>>>>>>>>>>
        url = f"https://api-metrika.yandex.net/stat/v1/data?dimensions=" \
              f"ym:s:trafficSource&metrics=ym:s:users,ym:s:goal%3Cgoal_id%3EconversionRate&goal_id=135514551&id={self.counter_number}"

        # All Goals
        # url = f"https://api-metrika.yandex.net/management/v1/counter/{self.counter_number}/goals"
        # The Goal
        # url = f"https://api-metrika.yandex.net/management/v1/counter/{self.counter_number}/goal/135514551"
        headers = {
            'Host': 'api-metrika.yandex.net',
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {YA_TOKEN}',
        }

        try:
            response = requests.get(url=url, headers=headers)
            data = response.json()
            logger.debug(data)
            return data
        except Exception as msg:
            logger.error(msg)


YANDEX_COUNTERS = 's'
YANDEX_COUNTER = '/{self.counter_number}'
YANDEX_GOALS = '/{self.counter_number}/goals'
YANDEX_GOAL = '/{self.counter_number}/goal/{goal_id}'


def start_ya_api():
    one = YandexAPInfo('67630381')
    ya_counters = one.get_info(YANDEX_COUNTERS)

    # === Counters ===
    # first = logger.info(ya_counters['counters'][0])
    # first_id = logger.info(ya_counters['counters'][1]['id'])
    # first_url = logger.info(ya_counters['counters'][0]['site'])
    # first_goals = logger.info(ya_counters['counters'][1]['code_options']['informer']['indicator'])

    # id = logger.info(ya_counters['goals'][0])

    # ya_counter = one.get_info(YANDEX_COUNTER)


if __name__ == '__main__':
    start_ya_api()


'https://oauth.yandex.ru/authorize?response_type=token&client_id=c6eb276fe80b44de9bfe8a277c096ce1'
'https://oauth.yandex.ru/verification_code#access_token=AgAAAABBdCeWAAbMeYE-_MuuCUPWtJV9O3SJVws&token_type=bearer&expires_in=31536000'
