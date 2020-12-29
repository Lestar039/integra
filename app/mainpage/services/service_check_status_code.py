import requests
from loguru import logger


class CheckStatusCode:

    def __init__(self, some_url):
        self.some_url = some_url

    def get_page(self):
        """
        Get HTML page
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) /'
                          'Chrome/74.0.3729.169 Safari/537.36'
        }
        try:
            return requests.get(self.some_url, headers=headers)
        except Exception as msg:
            logger.error(msg)

    def check_code_status(self, request):
        """
        Check status code
        """
        if request.status_code == 200:
            logger.debug(f'{self.some_url} - Success!')
            return True
        else:
            logger.error(f'{self.some_url} - not found')
            return False


def check_run():

    url_list = ['https://integra-auto.ru', 'https://integra-gk.ru',
                'http://integra-development.ru', 'http://integra-investment.ru',
                'http://integra-offers.ru', 'http://integra-arenda.ru',
                'http://how-to-invest.ru']
    result_list = list()

    for _ in url_list:
        one = CheckStatusCode(_)
        try:
            text = one.get_page()
            status = one.check_code_status(text)
            if status:
                result_list.append([_, 'Success!'])
        except Exception as msg:
            result_list.append([_, 'Error'])
            logger.error(msg)
    return result_list


if __name__ == "__main__":
    check_run()
