from django.urls import reverse, resolve
from django.test import SimpleTestCase
from analytics.views import *


class TestAnalyticsUrls(SimpleTestCase):
    """
    Test analytics urls: analytics page
    """

    def test_analytics_page_url(self):
        url = reverse('analytics_urls', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, analytics)
