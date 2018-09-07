from argus.libraries.tag_extractor import TagExtractor
import pytest
import tests.samples.loader as loader


class TestTagExtractor(object):
    @pytest.fixture
    def obj(self):
        obj = TagExtractor(loader.load_sample())
        return obj

    def test_browser(self, obj):
        assert obj.browser() == 'Chrome'

    def test_city(self, obj):
        assert obj.city() == 'Dulles'

    def test_connection(self, obj):
        assert obj.connection() == 'Cable'

    def test_country(self, obj):
        assert obj.country() == 'VA'

    def test_device(self, obj):
        pass

    def test_website(self, obj):
        assert obj.website() == 'http://www.barenecessities.com'
