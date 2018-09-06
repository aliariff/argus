from .ttfb import Ttfb
from .request_per_type import RequestPerType


class Builder(object):
    def __init__(self, data, *args, **kwargs):
        self.data = data
        self.args = args
        self.kwargs = kwargs

    def build(self):
        metrics = []
        for cls in [Ttfb, RequestPerType]:
            metrics.append(cls(self.data).build())
        return metrics
