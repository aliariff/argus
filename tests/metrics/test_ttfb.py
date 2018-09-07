
from argus.metrics.ttfb import Ttfb
import pytest
import tests.samples.loader as loader


class TestTtfb(object):
    @pytest.fixture
    def obj(self):
        obj = Ttfb(loader.load_sample())
        obj.run()
        return obj

    def test_measurement(self, obj):
        assert obj.measurement() == "ttfb"

    def test_is_valid(self, obj):
        assert obj.is_valid() == True

    def test_fields(self, obj):
        assert obj.fields() == {"value": 358.0}
