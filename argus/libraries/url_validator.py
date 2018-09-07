from bs4 import BeautifulSoup
import urllib


class UrlValidator(object):
    def __init__(self, url, html_body, *args, **kwargs):
        self.url = url
        self.html_body = html_body
        self.args = args
        self.kwargs = kwargs

    def get_test_ids(self):
        test_ids = []
        soup = BeautifulSoup(self.html_body, 'html.parser')
        tds = soup.find_all('td', {'class': 'url'})
        allowed_urls = self.get_allowed_urls()

        for td in tds:
            title = td.find('a')['title']
            if title in allowed_urls:
                test_id = td.find('a')['href'][8:-1]
                test_ids.append(test_id)
        return test_ids

    def get_allowed_urls(self):
        allowed_urls = []
        parsed_uri = urllib.parse.urlparse(self.url)
        if parsed_uri.scheme == '':
            allowed_urls.append('https://{}'.format(self.url))
            allowed_urls.append('http://{}'.format(self.url))
        else:
            allowed_urls.append(self.url)
        return allowed_urls
