import requests
from ..models import DomainData
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


def check_status_code():
    url_list = DomainData.objects.only('url')

    for _ in url_list:
        one = CheckStatusCode('https://' + str(_))
        two = CheckStatusCode('http://' + str(_))
        try:
            try:
                text = one.get_page()
                status = one.check_code_status(text)
                if status:
                    DomainData.objects.update_or_create(url=_, defaults={'status': 'Success', 'ssh': True})
                    logger.debug(f'{_} SSH - True')
            except Exception as msg:
                logger.error(msg)
                text = two.get_page()
                status = two.check_code_status(text)
                if status:
                    DomainData.objects.update_or_create(url=_, defaults={'status': 'Success'})
                    logger.debug(f'{_} Not SSH')
                else:
                    DomainData.objects.update_or_create(url=_, defaults={'status': 'Failed'})
                    logger.error(f'{_} Not found')
        except Exception as msg:
            logger.error(msg)
            DomainData.objects.update_or_create(url=_, defaults={'status': 'Failed'})


if __name__ == "__main__":
    check_status_code()
