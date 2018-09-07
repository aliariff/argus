from .base import Base


class Latency(Base):
    def fill(self):
        return self.default_fill()

    def is_valid(self):
        self.value = self.data['data'].get('latency')
        return self.value != None

    def measurement(self):
        return 'latency'

    def fields(self):
        return {
            "value": float(self.value)
        }
