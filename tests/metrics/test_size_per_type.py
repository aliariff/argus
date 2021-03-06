
from argus.metrics.size_per_type import SizePerType
import pytest
import tests.samples.loader as loader


class TestSizePerType(object):
    @pytest.fixture
    def obj(self):
        obj = SizePerType(loader.load_sample())
        return obj

    def test_measurement(self, obj):
        assert obj.measurement() == "size_per_type"

    def test_is_valid(self, obj):
        assert obj.is_valid() == True

    def test_fill(self, obj):
        assert obj.fill() == [
            {
                "fields": {"value": 167538},
                "measurement": "size_per_type",
                "tags": {
                    "browser": "Chrome",
                    "city": "North America",
                    "connection": "Cable",
                    "country": "USA",
                    "device": "Machine",
                    "extension": "html",
                    "id": "180904_HF_JMH",
                    "media_type": "text",
                    "region": "Dulles",
                    "website": "http://www.barenecessities.com",
                },
                "time": "2018-09-04T07:36:27Z",
            },
            {
                "fields": {"value": 35624},
                "measurement": "size_per_type",
                "tags": {
                    "browser": "Chrome",
                    "city": "North America",
                    "connection": "Cable",
                    "country": "USA",
                    "device": "Machine",
                    "extension": "css",
                    "id": "180904_HF_JMH",
                    "media_type": "text",
                    "region": "Dulles",
                    "website": "http://www.barenecessities.com",
                },
                "time": "2018-09-04T07:36:27Z",
            },
            {
                "fields": {"value": 202015},
                "measurement": "size_per_type",
                "tags": {
                    "browser": "Chrome",
                    "city": "North America",
                    "connection": "Cable",
                    "country": "USA",
                    "device": "Machine",
                    "extension": "javascript",
                    "id": "180904_HF_JMH",
                    "media_type": "application",
                    "region": "Dulles",
                    "website": "http://www.barenecessities.com",
                },
                "time": "2018-09-04T07:36:27Z",
            },
            {
                "fields": {"value": 92164},
                "measurement": "size_per_type",
                "tags": {
                    "browser": "Chrome",
                    "city": "North America",
                    "connection": "Cable",
                    "country": "USA",
                    "device": "Machine",
                    "extension": "font-woff2",
                    "id": "180904_HF_JMH",
                    "media_type": "application",
                    "region": "Dulles",
                    "website": "http://www.barenecessities.com",
                },
                "time": "2018-09-04T07:36:27Z",
            },
            {
                "fields": {"value": 340492},
                "measurement": "size_per_type",
                "tags": {
                    "browser": "Chrome",
                    "city": "North America",
                    "connection": "Cable",
                    "country": "USA",
                    "device": "Machine",
                    "extension": "javascript",
                    "id": "180904_HF_JMH",
                    "media_type": "text",
                    "region": "Dulles",
                    "website": "http://www.barenecessities.com",
                },
                "time": "2018-09-04T07:36:27Z",
            },
            {
                "fields": {"value": 290050},
                "measurement": "size_per_type",
                "tags": {
                    "browser": "Chrome",
                    "city": "North America",
                    "connection": "Cable",
                    "country": "USA",
                    "device": "Machine",
                    "extension": "webp",
                    "id": "180904_HF_JMH",
                    "media_type": "image",
                    "region": "Dulles",
                    "website": "http://www.barenecessities.com",
                },
                "time": "2018-09-04T07:36:27Z",
            },
            {
                "fields": {"value": 6907},
                "measurement": "size_per_type",
                "tags": {
                    "browser": "Chrome",
                    "city": "North America",
                    "connection": "Cable",
                    "country": "USA",
                    "device": "Machine",
                    "extension": "png",
                    "id": "180904_HF_JMH",
                    "media_type": "image",
                    "region": "Dulles",
                    "website": "http://www.barenecessities.com",
                },
                "time": "2018-09-04T07:36:27Z",
            },
            {
                "fields": {"value": 37949},
                "measurement": "size_per_type",
                "tags": {
                    "browser": "Chrome",
                    "city": "North America",
                    "connection": "Cable",
                    "country": "USA",
                    "device": "Machine",
                    "extension": "jpeg",
                    "id": "180904_HF_JMH",
                    "media_type": "image",
                    "region": "Dulles",
                    "website": "http://www.barenecessities.com",
                },
                "time": "2018-09-04T07:36:27Z",
            },
            {
                "fields": {"value": 813},
                "measurement": "size_per_type",
                "tags": {
                    "browser": "Chrome",
                    "city": "North America",
                    "connection": "Cable",
                    "country": "USA",
                    "device": "Machine",
                    "extension": "gif",
                    "id": "180904_HF_JMH",
                    "media_type": "image",
                    "region": "Dulles",
                    "website": "http://www.barenecessities.com",
                },
                "time": "2018-09-04T07:36:27Z",
            },
            {
                "fields": {"value": 130550},
                "measurement": "size_per_type",
                "tags": {
                    "browser": "Chrome",
                    "city": "North America",
                    "connection": "Cable",
                    "country": "USA",
                    "device": "Machine",
                    "extension": "x-javascript",
                    "id": "180904_HF_JMH",
                    "media_type": "application",
                    "region": "Dulles",
                    "website": "http://www.barenecessities.com",
                },
                "time": "2018-09-04T07:36:27Z",
            },
            {
                "fields": {"value": 19161},
                "measurement": "size_per_type",
                "tags": {
                    "browser": "Chrome",
                    "city": "North America",
                    "connection": "Cable",
                    "country": "USA",
                    "device": "Machine",
                    "extension": "json",
                    "id": "180904_HF_JMH",
                    "media_type": "application",
                    "region": "Dulles",
                    "website": "http://www.barenecessities.com",
                },
                "time": "2018-09-04T07:36:27Z",
            },
            {
                "fields": {"value": 0},
                "measurement": "size_per_type",
                "tags": {
                    "browser": "Chrome",
                    "city": "North America",
                    "connection": "Cable",
                    "country": "USA",
                    "device": "Machine",
                    "extension": "font-woff",
                    "id": "180904_HF_JMH",
                    "media_type": "application",
                    "region": "Dulles",
                    "website": "http://www.barenecessities.com",
                },
                "time": "2018-09-04T07:36:27Z",
            },
            {
                "fields": {"value": 131},
                "measurement": "size_per_type",
                "tags": {
                    "browser": "Chrome",
                    "city": "North America",
                    "connection": "Cable",
                    "country": "USA",
                    "device": "Machine",
                    "extension": "plain",
                    "id": "180904_HF_JMH",
                    "media_type": "text",
                    "region": "Dulles",
                    "website": "http://www.barenecessities.com",
                },
                "time": "2018-09-04T07:36:27Z",
            },
            {
                "fields": {"value": 0},
                "measurement": "size_per_type",
                "tags": {
                    "browser": "Chrome",
                    "city": "North America",
                    "connection": "Cable",
                    "country": "USA",
                    "device": "Machine",
                    "extension": "x-icon",
                    "id": "180904_HF_JMH",
                    "media_type": "image",
                    "region": "Dulles",
                    "website": "http://www.barenecessities.com",
                },
                "time": "2018-09-04T07:36:27Z",
            },
        ]
