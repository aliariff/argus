
from argus.metrics.speed_index import SpeedIndex
import pytest
import tests.samples.loader as loader


class TestSpeedIndex(object):
    @pytest.fixture
    def obj(self):
        obj = SpeedIndex(loader.load_sample())
        return obj

    def test_measurement(self, obj):
        assert obj.measurement() == "speed_index"

    def test_is_valid(self, obj):
        assert obj.is_valid() == True

    def test_fields(self, obj):
        assert obj.fields() == {"value": 1980.0}
