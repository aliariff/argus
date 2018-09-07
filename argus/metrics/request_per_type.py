from .base import Base
from collections import Counter


class RequestPerType(Base):
    def fill(self):
        self.requests = self.data["data"]["runs"]["1"]["firstView"]["requests"]
        request_counts = self.__count_request_per_type()

        metrics = []
        for key, value in request_counts.items():
            if key is None or key == "":
                continue

            metric = {
                "measurement": self.measurement(),
                "tags": {**self.tags(), **self._local_tags(key)},
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

    def _local_tags(self, key):
        try:
            media_type, extension = key.split("/")
            extension = extension.split(";", 1)[0]
            return {"media_type": media_type, "extension": extension}
        except:
            return {}
