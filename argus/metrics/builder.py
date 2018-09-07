from .ttfb import Ttfb
from .request_per_type import RequestPerType
from .response_time import ResponseTime

''' We should think about metrics with multiple values like TTFB(mean,media) !still not supported'''


class Builder(object):
    def __init__(self, data, *args, **kwargs):
        self.data = data
        self.args = args
        self.kwargs = kwargs

    def run(self):
        results = []
        metrics = [cls(self.data).run()
                   for cls in [Ttfb, RequestPerType, ResponseTime, DomElements, FullyLoaded, \
                   Latency, LoadTime, RenderStart, SpeedIndex]]
        for metric in metrics:
            if metric is None:
                continue
            elif isinstance(metric, list):
                [results.append(x) for x in metric]
            else:
                results.append(metric)

        return results
