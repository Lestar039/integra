from django.urls import reverse, resolve
from django.test import SimpleTestCase
from mainpage.views import *


class TestGeneralUrls(SimpleTestCase):
    """
    Test general urls: index
    """

    def test_index_page_url(self):
        url = reverse('index_url')
        self.assertEqual(resolve(url).func, index)
