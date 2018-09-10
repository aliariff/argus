
from argus.metrics.render_start import RenderStart
import pytest
import tests.samples.loader as loader


class TestRenderStart(object):
    @pytest.fixture
    def obj(self):
        obj = RenderStart(loader.load_sample())
        return obj

    def test_measurement(self, obj):
        assert obj.measurement() == "render_start"

    def test_is_valid(self, obj):
        assert obj.is_valid() == True

    def test_fields(self, obj):
        assert obj.fields() == {"value": 1500.0}
