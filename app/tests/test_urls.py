from django.urls import reverse, resolve
from django.test import SimpleTestCase
from analytics.views import *
from mainpage.views import *
from web_service.views import *


class TestGeneralUrls(SimpleTestCase):
    """
    Test general urls: index, redirect after login, dashboard
    """

    def test_index_page_url(self):
        url = reverse('index_url')
        self.assertEqual(resolve(url).func, index)

    def test_user_page_url(self):
        url = reverse('redirect_to_user_page')
        self.assertEqual(resolve(url).func, redirect_to_user_page)

    def test_dashboard_url(self):
        url = reverse('dashboard_urls', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, dashboard)


class TestHostingUrls(SimpleTestCase):
    """
    Test hosting urls: hosting page, edit, delete
    """

    def test_hosting_page_url(self):
        url = reverse('hosting_urls', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, save_hosting)

    def test_edit_hosting_page_url(self):
        url = reverse('hosting_edit_urls', kwargs={'pk': 1, 'name_ed': 'some_name'})
        self.assertEqual(resolve(url).func, edit_hosting)

    def test_delete_hosting_url(self):
        url = reverse('hosting_delete_urls', kwargs={'pk': 1, 'name_del': 'some_name'})
        self.assertEqual(resolve(url).func, delete_hosting)


class TestDomainUrls(SimpleTestCase):
    """
    Test domain urls: domain page, edit, delete
    """

    def test_domain_page_url(self):
        url = reverse('domains_urls', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, save_domain)

    def test_edit_domain_page_url(self):
        url = reverse('domain_edit_urls', kwargs={'pk': 1, 'url_ed': 'some_name'})
        self.assertEqual(resolve(url).func, edit_domain)

    def test_delete_domain_url(self):
        url = reverse('domain_delete_urls', kwargs={'pk': 1, 'url_del': 'some_name'})
        self.assertEqual(resolve(url).func, delete_domain)


class TestAnalyticsUrls(SimpleTestCase):
    """
    Test analytics urls: analytics page
    """

    def test_analytics_page_url(self):
        url = reverse('analytics_urls', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, analytics)
