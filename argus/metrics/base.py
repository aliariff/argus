import datetime
from argus.libraries.tag_extractor import TagExtractor


class Base(object):
    def __init__(self, data, *args, **kwargs):
        self.data = data
        self.args = args
        self.kwargs = kwargs

    def run(self):
        if self.is_valid():
            return self.fill()
        else:
            return None

    def default_fill(self):
        return {
            "measurement": self.measurement(),
            "tags": self.tags(),
            "time": self.time(),
            "fields": self.fields(),
        }

    def get_value_from_column(self, key):
        data = self.data["data"]["average"]["firstView"]
        if isinstance(data, dict):
            return data.get(key)
        return None

    def fill(self):
        raise NotImplementedError()

    def fields(self):
        raise NotImplementedError()

    def is_valid(self):
        raise NotImplementedError()

    def measurement(self):
        raise NotImplementedError()

    def tags(self):
        return TagExtractor(self.data).extract()

    def time(self):
        timestamp = datetime.datetime.fromtimestamp(self.data["data"]["completed"])
        return timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
