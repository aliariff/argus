class Base(object):
    def __init__(self, data, *args, **kwargs):
        self.data = data
        self.args = args
        self.kwargs = kwargs

    def build(self):
        {
            "measurement": self.measurement(),
            "tags": self.tags(),
            "time": self.time(),
            "fields": self.fields()
        }

    def measurement(self):
        raise NotImplementedError()

    def tags(self):
        pass

    def time(self):
        pass

    def fields(self):
        raise NotImplementedError()
