from .base import Base
from collections import Counter


class RequestPerType(Base):
    def measurement(self):
        return 'request_per_type'

    def fields(self):
        return self.__count_request_per_type()

    def __count_request_per_type(self):
        requests = self.data['data']['runs']['1']['firstView']['requests']
        results = Counter([request.get('contentType')
                           or 'other' for request in requests])
        return dict(results)
