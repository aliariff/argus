from bs4 import BeautifulSoup
import aiohttp
import coloredlogs
import logging
import requests

logger = logging.getLogger(__name__)
coloredlogs.install()


def get_test_ids(url, days):
    page = requests.get('https://www.webpagetest.org/testlog.php?days=' +
                        str(days)+'&filter='+url+'&all=on&nolimit=on')
    soup = BeautifulSoup(page.content, 'html.parser')
    tds = soup.find_all('td', {'class': 'url'})
    return [td.find('a')['href'][8:-1] for td in tds]


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
