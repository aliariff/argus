import click
import requests as re
import datetime
from bs4 import BeautifulSoup
from influxdb import InfluxDBClient

client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')
client.create_database('example')
result = client.query('select value from ttfb;')
print result


@click.group()
def cli():
    pass


@cli.command()
@click.option('--url', default=[])
@click.option('--days', default=1)
def populate(url, days):
    ids = getTestIDs(url, days)
    for id_ in ids:
        print('\nid:{}\n'.format(id_))
        data = getData(id_)
        timestamp = datetime.datetime.fromtimestamp(data['completed'])
        client.write_points([
            {
                "measurement": "ttfb",
                "tags": {},
                "time": timestamp.strftime('%Y-%m-%dT%H:%M:%SZ'),
                "fields": {
                    "value": float(data['TTFB_mean'])
                }
            }
        ])


def getTestIDs(url, days):
    page = re.get('https://www.webpagetest.org/testlog.php?days=' +
                  str(days)+'&filter='+url+'&all=on')
    soup = BeautifulSoup(page.content, 'html.parser')
    tds = soup.find_all('td', {'class': 'url'})
    return [td.find('a')['href'][8:-1] for td in tds]


def getData(test_id):
    out = {}
    data = re.get(
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
