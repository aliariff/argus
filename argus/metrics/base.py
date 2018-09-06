import datetime
from argus.libraries.tag_extractor import TagExtractor


class Base(object):
    def __init__(self, data, *args, **kwargs):
        self.data = data
        self.args = args
        self.kwargs = kwargs

    def run(self):
        if self.is_valid():
            return self.build()
        else:
            return None

    def build(self):
        raise NotImplementedError()

    def is_valid(self):
        raise NotImplementedError()

    def measurement(self):
        raise NotImplementedError()

    def tags(self):
        return TagExtractor(self.data).extract()

    def time(self):
        timestamp = datetime.datetime.fromtimestamp(
            self.data['data']['completed'])
        return timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')
