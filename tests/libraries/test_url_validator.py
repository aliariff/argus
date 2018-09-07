from argus.libraries.url_validator import UrlValidator


class TestUrlValidator(object):
    def test_without_protocol(self):
        result = UrlValidator('abc.com', '').get_allowed_urls()
        assert result == ['https://abc.com', 'http://abc.com']
