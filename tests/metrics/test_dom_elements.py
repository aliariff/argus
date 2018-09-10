
from argus.metrics.dom_elements import DomElements
import pytest
import tests.samples.loader as loader


class TestDomElements(object):
    @pytest.fixture
    def obj(self):
        obj = DomElements(loader.load_sample())
        return obj

    def test_measurement(self, obj):
        assert obj.measurement() == "DOM_elements"

    def test_is_valid(self, obj):
        assert obj.is_valid() == True

    def test_fields(self, obj):
        assert obj.fields() == {"value": 3570.0}
