import asyncio
import argus.fetchers.webpagetest as webpagetest
import argus.db.influxdb as influxdb
from argus.metrics.ttfb import Ttfb


def run(url, days):
    loop = asyncio.get_event_loop()
    ids = webpagetest.get_test_ids(url, days)

    futures = []
    for id_ in ids:
        futures.append(__process(id_))
    loop.run_until_complete(asyncio.wait(futures))


async def __process(test_id):
    data = await webpagetest.get_result(test_id)
    metric = Ttfb(data).build()
    print(metric)
    influxdb.client().write_points([metric])
    return
