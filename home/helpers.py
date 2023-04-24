import datetime

from django.core.cache import cache
from bs4 import BeautifulSoup
from django.conf import settings
import requests


def get_jar_info() -> dict | None:
    """
    Get information about donations to monobank jar for pay to server.
    """

    jar_info: dict | None = cache.get('monobank_jar_info', None)
    if jar_info is not None:
        return jar_info
    else:
        jar_info = {}

    response = requests.get(
        url='https://api.monobank.ua/personal/client-info',
        headers={
            'X-Token': settings.MONOBANK_PERSONAL_API_TOKEN
        }
    )
    if response.status_code != 200:
        return None

    response = response.json()
    try:
        jar = [jar for jar in response['jars'] if jar['sendId'] == settings.MONOBANK_JAR_SEND_ID]

        if len(jar) != 1:
            raise KeyError
        else:
            jar = jar[0]

        jar_info['accumulated'] = float(jar['balance']/100)
        jar_info['goal'] = float(jar['goal']/100)
    except KeyError:
        return None

    cache.set('monobank_jar_info', jar_info, 60)

    return jar_info


def get_donate_jar_box_info() -> dict:
    """
    Get all data such:
    - jar accumulated
    - jar goal
    - users count
    - first day of period
    - last day of period
    - per user pay
    for donate ox in the home page.
    """

    donate_box_data: dict = {

    }

    jar_info: dict | None = get_jar_info()

    if jar_info is None:
        donate_box_data['jar'] = {
            'accumulated': 'Unknown',
            'goal': 'Unknown',
        }
    else:
        donate_box_data['jar'] = jar_info

    today: datetime.date = datetime.datetime.today()
    first_period_day: datetime.date = today.replace(day=1)
    donate_box_data['first_period_day'] = first_period_day

    last_period_day = first_period_day.replace(month=first_period_day.month+1)
    last_period_day = last_period_day - datetime.timedelta(days=1)
    donate_box_data['last_period_day'] = last_period_day

    response = requests.get(
        url='https://matrix.opulus.space/_synapse/admin/v2/users',
        headers={
            'Authorization': f'Bearer {settings.MATRIX_TOKEN}'
        }
    )
    if response.status_code != 200:
        donate_box_data['users_count'] = 'Unknown'
        donate_box_data['per_user_pay'] = 'Unknown'
    elif jar_info is None:
        donate_box_data['users_count'] = int(response.json()['total'])
        donate_box_data['per_user_pay'] = 'Unknown'
    else:
        users_count: int = int(response.json()['total'])
        donate_box_data['users_count'] = users_count
        donate_box_data['per_user_pay'] = float(jar_info['goal']/users_count)

    return donate_box_data

