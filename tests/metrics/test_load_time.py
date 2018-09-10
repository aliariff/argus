
from argus.metrics.load_time import LoadTime
import pytest
import tests.samples.loader as loader


class TestLoadTime(object):
    @pytest.fixture
    def obj(self):
        obj = LoadTime(loader.load_sample())
        return obj

    def test_measurement(self, obj):
        assert obj.measurement() == "load_time"

    def test_is_valid(self, obj):
        assert obj.is_valid() == True

    def test_fields(self, obj):
        assert obj.fields() == {"value": 4766.0}
