class Service(object):
    @classmethod
    def execute(cls, inputs, files=None, **kwargs):
        instance = cls(inputs, files, **kwargs)
        return instance.run()

    def run(self):
        raise NotImplementedError()
