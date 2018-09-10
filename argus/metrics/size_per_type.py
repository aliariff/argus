from .base import Base
from collections import Counter


class SizePerType(Base):
    def fill(self):
        self.requests = self.data["data"]["runs"]["1"]["firstView"]["requests"]
        request_size = self.__sum_request_size_per_type()

        metrics = []
        for key, value in request_size.items():
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
        return "size_per_type"

    def __sum_request_size_per_type(self):
        sum_size = {}
        for req in self.requests:
            content_type = req.get("contentType")
            if content_type in sum_size:
                sum_size[content_type] += req.get("objectSize")
            else:
                sum_size[content_type] = 0
        return sum_size

    def _local_tags(self, key):
        try:
            media_type, extension = key.split("/")
            extension = extension.split(";", 1)[0]
            return {"media_type": media_type, "extension": extension}
        except:
            return {}
