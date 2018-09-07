import re
import urllib


class TagExtractor(object):
    def __init__(self, data, *args, **kwargs):
        self.data = data
        self.args = args
        self.kwargs = kwargs

    def extract(self):
        return {
            "browser": self.browser(),
            "city": self.city(),
            "connection": self.connection(),
            "country": self.country(),
            "device": self.device(),
            "website": self.website()
        }

    def browser(self):
        return self.data['data']['location'].split(':')[1]

    def city(self):
        temp = self.data['data']['from'].split()
        if temp[1] == '-':
            return None
        else:
            return re.sub("[^a-zA-Z]+", "", temp[0])

    def connection(self):
        return self.data['data']['connectivity']

    def country(self):
        temp = self.data['data']['from'].split()
        if temp[1] == '-':
            return temp[0]
        else:
            return temp[1]

    def device(self):
        pass

    def website(self):
        parsed_uri = urllib.parse.urlparse(self.data['data']['url'])
        if parsed_uri.scheme != '':
            return '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri).lower()
        else:
            return self.data['data']['url'].rstrip('/').lower()
