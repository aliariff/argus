import click
import datetime
import argus.fetchers.webpagetest as webpagetest
from influxdb import InfluxDBClient

client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')
client.create_database('example')
result = client.query('select value from ttfb;')
print(result)


@click.group()
def cli():
    pass


@cli.command()
@click.option('--url', default=[])
@click.option('--days', default=1)
def populate(url, days):
    click.echo('Fetching tests of {} for the last {} days ...'.format(url,days))
    ids = webpagetest.get_test_ids(url, days)
    click.echo('{} tests have been found'.format(len(ids)))
    for id_ in ids:
        #print('\nid:{}\n'.format(id_))
        data = webpagetest.get_result(id_)
        timestamp = datetime.datetime.fromtimestamp(data['completed'])
        click.echo('Pushing data to influxdb...')
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
