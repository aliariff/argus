from argus.db.influxdb import InfluxDB
from argus.metrics.builder import Builder
import argus.fetchers.webpagetest as webpagetest
import asyncio
import coloredlogs
import logging

logger = logging.getLogger(__name__)
coloredlogs.install()


def run(url, days):
    logger.info('Fetching tests of {} for the last {} days'.format(url, days))
    ids = webpagetest.get_test_ids(url, days)
    logger.info('Test ids {}'.format(ids))

    futures = []
    for id_ in ids:
        futures.append(__process(id_))

    if futures:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(futures))


async def __process(test_id):
    logger.info('Get data from test {}'.format(test_id))
    data = await webpagetest.get_result(test_id)
    if data.get('statusCode') != 200:
        logger.error('Get data failed {}'.format(test_id))
        return

    logger.info('Building metric for test {}'.format(test_id))
    metrics = Builder(data).run()

    logger.info('Saving metric for test {}, size: {}'.format(
        test_id, len(metrics)))
    InfluxDB().save(metrics)

    return
