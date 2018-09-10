
from argus.metrics.latency import Latency
import pytest
import tests.samples.loader as loader


class TestLatency(object):
    @pytest.fixture
    def obj(self):
        obj = Latency(loader.load_sample())
        return obj

    def test_measurement(self, obj):
        assert obj.measurement() == "latency"

    def test_is_valid(self, obj):
        assert obj.is_valid() == True

    def test_fields(self, obj):
        assert obj.fields() == {"value": 28.0}
