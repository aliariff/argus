import re
import urllib


class TagExtractor(object):
    def __init__(self, data, *args, **kwargs):
        self.data = data
        self.args = args
        self.kwargs = kwargs

    def extract(self):
        return {
            "browser": self.__browser(),
            "city": self.__city(),
            "connection": self.__connection(),
            "country": self.__country(),
            "device": self.__device(),
            "website": self.__website()
        }

    def __browser(self):
        return self.data['data']['location'].split(':')[1]

    def __city(self):
        temp = self.data['data']['from'].split()
        if temp[1] == '-':
            return None
        else:
            return re.sub("[^a-zA-Z]+", "", temp[0])

    def __connection(self):
        return self.data['data']['connectivity']

    def __country(self):
        temp = self.data['data']['from'].split()
        if temp[1] == '-':
            return temp[0]
        else:
            return temp[1]

    def __device(self):
        pass

    def __website(self):
        parsed_uri = urllib.parse.urlparse(self.data['data']['url'])
        return '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri).lower()
