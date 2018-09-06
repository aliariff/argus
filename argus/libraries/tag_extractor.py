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
        pass

    def city(self):
        pass

    def connection(self):
        pass

    def country(self):
        pass

    def device(self):
        pass

    def website(self):
        pass
