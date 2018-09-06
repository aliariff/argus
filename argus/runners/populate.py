import asyncio
import argus.fetchers.webpagetest as webpagetest
from argus.db.influxdb import InfluxDB
from argus.metrics.builder import Builder


def run(url, days):
    print('Fetching tests of {} for the last {} days'.format(url, days))
    ids = webpagetest.get_test_ids(url, days)
    print('Test ids {}'.format(ids))

    futures = []
    for id_ in ids:
        futures.append(__process(id_))

    if futures:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(futures))


async def __process(test_id):
    print('Get data from test {}'.format(test_id))
    data = await webpagetest.get_result(test_id)
    if data['statusCode'] != 200:
        print('Get data failed {}'.format(test_id))
        return

    print('Building metric for test {}'.format(test_id))
    metrics = Builder(data).run()

    print('Saving metric for test {}, size: {}'.format(test_id, len(metrics)))
    InfluxDB().save(metrics)

    return
