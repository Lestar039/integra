from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.html import format_html

from ..models import DomainData, HostingData
from .bot_config import INTEGRA_DATE_BOT
from datetime import datetime, timezone
import requests
from loguru import logger


def check_telegram_id(request, pk):
    """
    Check user telegram ID
    """
    user = User.objects.get(id=pk)
    if user.profile.telegram_id:
        logger.debug(f'User {user} have telegram ID')
        return False
    else:
        logger.debug(f"User {user} don't have telegram ID")
        messages.error(
            request,
            format_html("You won't receive any alerts, \
            \nas you haven't set the Telegram chat ID in your Profile yet.\n \
            Please, contact <a href='https://t.me/integra_date_bot'>t.me/integra_date_bot</a> to find out your chat ID."))

        return True


def _send_alert_to_telegram(some_service, user_telegram_id, some_days, some_name):
    """
    Send alert message to telegram
    """
    bot_id = INTEGRA_DATE_BOT
    text = f"Attention! {some_name}: '{some_service}' left in '{some_days}' days"

    if user_telegram_id:
        url = f"https://api.telegram.org/bot{bot_id}/sendMessage?chat_id={user_telegram_id}&text={text}"
        requests.get(url)
        logger.debug('Send alert!')


def domain_time_comparison():
    """
    Create expiration time list domains
    """
    all_urls = DomainData.objects.only('url', 'expiration_date')
    time_now = datetime.now(timezone.utc)
    expiration_list = list()

    for _ in all_urls:
        delta = _.expiration_date - time_now
        if delta.days <= 7:
            expiration_list.append([_.url, delta.days])

            _send_alert_to_telegram(_.url, _.username.profile.telegram_id, delta.days, 'Domain')

    return expiration_list


def hosting_time_comparison():
    """
    Create expiration time list hosting
    """
    all_urls = HostingData.objects.only('name', 'expiration_date')
    time_now = datetime.now(timezone.utc)
    expiration_list = list()

    for _ in all_urls:
        delta = _.expiration_date - time_now
        if delta.days <= 7:
            expiration_list.append([_.name, delta.days])

            _send_alert_to_telegram(_.name, _.username.profile.telegram_id, delta.days, 'Hosting')

    return expiration_list
