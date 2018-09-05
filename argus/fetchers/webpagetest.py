from bs4 import BeautifulSoup
import aiohttp
import requests


def get_test_ids(url, days):
    page = requests.get('https://www.webpagetest.org/testlog.php?days=' +
                        str(days)+'&filter='+url+'&all=on')
    soup = BeautifulSoup(page.content, 'html.parser')
    tds = soup.find_all('td', {'class': 'url'})
    return [td.find('a')['href'][8:-1] for td in tds]


async def get_result(test_id):
    try:
        print('Get data from test {}'.format(test_id))
        session = aiohttp.ClientSession()
        response = await session.get('https://www.webpagetest.org/jsonResult.php?test='+test_id)
        data = await response.json()
        await session.close()
        return data
    except:
        print(data)
