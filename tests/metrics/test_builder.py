
from argus.metrics.builder import Builder
import pytest
import tests.samples.loader as loader


class TestBuilder(object):
    @pytest.fixture
    def obj(self):
        obj = Builder(loader.load_sample())
        return obj

    def test_run(self, obj):
        assert isinstance(obj.run(), list) == True
