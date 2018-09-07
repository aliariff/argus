import argus.fetchers.webpagetest as webpagetest
import httpretty
import re
import asyncio
import json


@httpretty.activate
def test_get_test_ids():
    httpretty.register_uri(
        httpretty.GET,
        re.compile(r'https://www.webpagetest.org/.*'),
        body='''
          <td class="url"><a title="http://abc.com" href="/result/123/">http://abc.com</a></td>
          <td class="url"><a title="http://abc.com" href="/result/456/">http://abc.com</a></td>
          <td class="url"><a title="http://abc.com" href="/result/789/">http://abc.com</a></td>
        '''
    )

    ids = webpagetest.get_test_ids('abc.com', '1')
    assert ids == ['123', '456', '789']


@httpretty.activate
def test_get_result():
    httpretty.register_uri(
        httpretty.GET,
        re.compile(r'https://www.webpagetest.org/.*'),
        body=json.dumps({})
    )

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(webpagetest.get_result('123'))

    assert result == {}
