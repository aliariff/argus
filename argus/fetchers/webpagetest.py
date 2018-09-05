import requests
from bs4 import BeautifulSoup


def get_test_ids(url, days):
    page = requests.get('https://www.webpagetest.org/testlog.php?days=' +
                        str(days)+'&filter='+url+'&all=on')
    soup = BeautifulSoup(page.content, 'html.parser')
    tds = soup.find_all('td', {'class': 'url'})
    return [td.find('a')['href'][8:-1] for td in tds]


def get_result(test_id):
    out = {}
    data = requests.get(
        'https://www.webpagetest.org/jsonResult.php?test='+test_id).json()
    out['TTFB_mean'] = data['data']['average']['firstView']['TTFB']
    out['TTFB_median'] = data['data']['average']['firstView']['TTFB']
    out['connectivity'] = data['data']['connectivity']
    out['id'] = data['data']['id']
    out['from'] = data['data']['from']
    out['location'] = data['data']['location']
    out['mobile'] = data['data']['mobile']
    out['completed'] = data['data']['completed']
    return out
