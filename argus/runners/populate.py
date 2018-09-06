import asyncio
import argus.fetchers.webpagetest as webpagetest
from argus.db.influxdb import InfluxDB
from argus.metrics.builder import Builder


def run(url, days):
    loop = asyncio.get_event_loop()

    print('Fetching tests of {} for the last {} days'.format(url, days))
    ids = webpagetest.get_test_ids(url, days)
    print('Test ids found {}'.format(ids))

    futures = []
    for id_ in ids:
        futures.append(__process(id_))

    if futures:
        loop.run_until_complete(asyncio.wait(futures))


async def __process(test_id):
    print('Get data from test {}'.format(test_id))
    data = await webpagetest.get_result(test_id)

    print('Building metric for test {}'.format(test_id))
    metrics = Builder(data).build

    print('Saving metric for test {}'.format(test_id))
    InfluxDB().save(metrics)

    return
