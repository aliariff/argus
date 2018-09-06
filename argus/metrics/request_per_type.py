from .base import Base


class RequestPerType(Base):
    def measurement(self):
        return 'request_per_type'

    def fields(self):
        return {
            "js": 0,
            "css": 1,
            "img": 2
        }
