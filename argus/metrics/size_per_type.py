from .base import Base
from collections import Counter


class SizePerType(Base):
    def fill(self):
        request_size = self.__sum_request_size_per_type()

        metrics = []
        for key, value in request_size.items():
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
        return "size_per_type"

    def __sum_request_size_per_type(self):
        sum_size = {}
        for req in self.requests:
            content_type = req.get("contentType")
            if content_type in sum_size:
                object_size = req.get("objectSize")
                if object_size != "" and object_size is not None:
                    sum_size[content_type] += int(object_size)
            else:
                sum_size[content_type] = 0
        return sum_size
