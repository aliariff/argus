
from argus.metrics.fully_loaded import FullyLoaded
import pytest
import tests.samples.loader as loader


class TestFullyLoaded(object):
    @pytest.fixture
    def obj(self):
        obj = FullyLoaded(loader.load_sample())
        return obj

    def test_measurement(self, obj):
        assert obj.measurement() == "fully_loaded"

    def test_is_valid(self, obj):
        assert obj.is_valid() == True

    def test_fields(self, obj):
        assert obj.fields() == {"value": 6309.0}
