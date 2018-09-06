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
        pass

    def __city(self):
        pass

    def __connection(self):
        pass

    def __country(self):
        pass

    def __device(self):
        pass

    def __website(self):
        pass
