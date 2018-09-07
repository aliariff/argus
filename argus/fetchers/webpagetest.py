import aiohttp
import coloredlogs
import logging
import requests
from argus.libraries.url_validator import UrlValidator

logger = logging.getLogger(__name__)
coloredlogs.install()


def get_test_ids(url, days):
    page = requests.get('https://www.webpagetest.org/testlog.php?days=' +
                        str(days)+'&filter='+url+'&all=on&nolimit=on')
    return UrlValidator(url, page.content).get_test_ids()


async def get_result(test_id):
    session = aiohttp.ClientSession()
    data = {}
    try:
        response = await session.get('https://www.webpagetest.org/jsonResult.php?test='+test_id)
        data = await response.json()
    except Exception as error:
        logging.error(
            'Error: get_result {} {}'.format(test_id, error))
    finally:
        await session.close()
        return data
