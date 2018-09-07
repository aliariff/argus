from argus.libraries.tag_extractor import TagExtractor


class TestTagExtractor(object):
    def test_browser(self):
        data = {
            'data': {
                'location': 'Dulles:Chrome'
            }
        }
        assert TagExtractor(data).browser() == 'Chrome'
