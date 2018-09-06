import datetime
from argus.libraries.tag_extractor import TagExtractor


class Base(object):
    def __init__(self, data, *args, **kwargs):
        self.data = data
        self.args = args
        self.kwargs = kwargs

    def build(self):
        return {
            "measurement": self.measurement(),
            "tags": self.tags(),
            "time": self.time(),
            "fields": self.fields()
        }

    def measurement(self):
        raise NotImplementedError()

    def tags(self):
        TagExtractor(self.data).extract()

    def time(self):
        timestamp = datetime.datetime.fromtimestamp(
            self.data['data']['completed'])
        return timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')

    def fields(self):
        raise NotImplementedError()
