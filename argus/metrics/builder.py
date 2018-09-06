from .ttfb import Ttfb
from .request_per_type import RequestPerType


class Builder(object):
    def __init__(self, data, *args, **kwargs):
        self.data = data
        self.args = args
        self.kwargs = kwargs

    def build(self):
        return [cls(self.data).build() for cls in [Ttfb, RequestPerType]]
