from .base import Base
from collections import Counter


class ResponseCode(Base):
    def fill(self):
        return {
            "measurement": self.measurement(),
            "tags": self.tags(),
            "time": self.time(),
            "fields": self.__count_response_code(),
        }

    def is_valid(self):
        return len(self.__count_response_code()) > 0

    def measurement(self):
        return "response_code"

    def __count_response_code(self):
        self.requests = self.data["data"]["runs"]["1"]["firstView"]["requests"]
        results = Counter([request.get("responseCode") for request in self.requests])
        return dict(results)
