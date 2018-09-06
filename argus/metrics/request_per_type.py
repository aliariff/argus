from .base import Base


class RequestPerType(Base):
    def measurement(self):
        return 'request_per_type'

    def fields(self):
        return self.__count_request_per_type()

    def __count_request_per_type(self):
        result = {}
        for req in self.data['request']:
            if req['content_type'] == 'html':
                result['html'] += 1
            elif req['content_type'] == 'css':
                result['css'] += 1

        return result
