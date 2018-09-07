from argus.libraries.url_validator import UrlValidator


class TestUrlValidator(object):
    def test_without_protocol(self):
        result = UrlValidator("abc.com", "").get_allowed_urls()
        assert result == ["abc.com", "https://abc.com", "http://abc.com"]

        result = UrlValidator("www.abc.com", "").get_allowed_urls()
        assert result == ["www.abc.com", "https://www.abc.com", "http://www.abc.com"]

    def test_with_protocol(self):
        result = UrlValidator("https://abc.com", "").get_allowed_urls()
        assert result == ["https://abc.com"]

        result = UrlValidator("http://abc.com", "").get_allowed_urls()
        assert result == ["http://abc.com"]

    def test_with_path(self):
        result = UrlValidator("https://abc.com/xyz", "").get_allowed_urls()
        assert result == ["https://abc.com/xyz"]

        result = UrlValidator("http://abc.com/xyz", "").get_allowed_urls()
        assert result == ["http://abc.com/xyz"]

        result = UrlValidator("abc.com/xyz", "").get_allowed_urls()
        assert result == ["abc.com/xyz", "https://abc.com/xyz", "http://abc.com/xyz"]

        result = UrlValidator("www.abc.com/xyz", "").get_allowed_urls()
        assert result == [
            "www.abc.com/xyz",
            "https://www.abc.com/xyz",
            "http://www.abc.com/xyz",
        ]

    def test_normalize_url(self):
        assert "abc.com" == UrlValidator("", "").normalize_url("abc.com//")
        assert "abc.com" == UrlValidator("", "").normalize_url("ABC.com//")
        assert "abc.com/xyz" == UrlValidator("", "").normalize_url("ABC.com/xyz/")
        assert "https://www.abc.com" == UrlValidator("", "").normalize_url(
            "https://www.ABC.com//"
        )
