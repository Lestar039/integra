from mainpage.services.service_check_status_code import CheckStatusCode
from django.test import TestCase

from loguru import logger


class TestStatusCode(TestCase):
    logger.debug('Start tests status code')

    def test_integra_auto(self):
        one = CheckStatusCode('https://integra-auto.ru')
        text = one.get_page()
        self.assertEqual(one.check_code_status(text), True)

    def test_integra_gk(self):
        one = CheckStatusCode('https://integra-gk.ru')
        text = one.get_page()
        self.assertEqual(one.check_code_status(text), True)

    def test_integra_development(self):
        one = CheckStatusCode('http://integra-development.ru')
        text = one.get_page()
        self.assertEqual(one.check_code_status(text), True)

    def test_integra_investment(self):
        one = CheckStatusCode('http://integra-investment.ru')
        text = one.get_page()
        self.assertEqual(one.check_code_status(text), True)

    def test_integra_offers(self):
        one = CheckStatusCode('http://integra-offers.ru')
        text = one.get_page()
        self.assertEqual(one.check_code_status(text), True)

    def test_integra_arenda(self):
        one = CheckStatusCode('http://integra-arenda.ru')
        text = one.get_page()
        self.assertEqual(one.check_code_status(text), True)

    def test_how_to_invest(self):
        one = CheckStatusCode('http://how-to-invest.ru')
        text = one.get_page()
        self.assertEqual(one.check_code_status(text), True)

