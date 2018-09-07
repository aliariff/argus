import json
import os
from argus.libraries.tag_extractor import TagExtractor


class TestTagExtractor(object):
    def load_data(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "../samples/test_result.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        with open(abs_file_path) as f:
            return json.load(f)

    def test_browser(self):
        assert TagExtractor(self.load_data()).browser() == 'Chrome'

    def test_city(self):
        assert TagExtractor(self.load_data()).city() == 'Dulles'

    def test_connection(self):
        assert TagExtractor(self.load_data()).connection() == 'Cable'

    def test_country(self):
        assert TagExtractor(self.load_data()).country() == 'VA'

    def test_device(self):
        pass

    def test_website(self):
        assert TagExtractor(self.load_data()).website(
        ) == 'http://www.barenecessities.com'
