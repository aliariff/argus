
from argus.metrics.response_code import ResponseCode
import pytest
import tests.samples.loader as loader


class TestResponseCode(object):
    @pytest.fixture
    def obj(self):
        obj = ResponseCode(loader.load_sample())
        return obj

    def test_measurement(self, obj):
        assert obj.measurement() == "response_code"

    def test_is_valid(self, obj):
        assert obj.is_valid() == True

    def test_fill(self, obj):
        assert obj.fill() == {
            "fields": {200: 168, 204: 1, 301: 1, 302: 1},
            "measurement": "response_code",
            "tags": {
                "browser": "Chrome",
                "city": "North America",
                "connection": "Cable",
                "country": "USA",
                "device": "Machine",
                "id": "180904_HF_JMH",
                "region": "Dulles",
                "website": "http://www.barenecessities.com",
            },
            "time": "2018-09-04T07:36:27Z",
        }
