from .base import Base
from collections import Counter


class RequestPerType(Base):
    def fill(self):
        request_counts = self.__count_request_per_type()

        metrics = []
        for key, value in request_counts.items():
            if key is None or key == "":
                continue

            metric = {
                "measurement": self.measurement(),
                "tags": {**self.default_tags(), **self.media_type_tags(key)},
                "time": self.time(),
                "fields": {"value": value},
            }
            metrics.append(metric)

        return metrics

    def is_valid(self):
        return True

    def measurement(self):
        return "request_per_type"

    def __count_request_per_type(self):
        results = Counter([request.get("contentType") for request in self.requests])
        return dict(results)
