from .ttfb import Ttfb
from .request_per_type import RequestPerType
from .dom_elements import DomElements
from .fully_loaded import FullyLoaded
from .latency import Latency
from .load_time import LoadTime
from .render_start import RenderStart
from .speed_index import SpeedIndex


""" We should think about metrics with multiple values like TTFB(mean,media) !still not supported"""


class Builder(object):
    def __init__(self, data, *args, **kwargs):
        self.data = data
        self.args = args
        self.kwargs = kwargs

    def run(self):
        results = []
        metrics = [
            cls(self.data).run()
            for cls in [
                Ttfb,
                RequestPerType,
                DomElements,
                FullyLoaded,
                Latency,
                LoadTime,
                RenderStart,
                SpeedIndex,
            ]
        ]
        for metric in metrics:
            if metric is None:
                continue
            elif isinstance(metric, list):
                [results.append(x) for x in metric]
            else:
                results.append(metric)

        return results
