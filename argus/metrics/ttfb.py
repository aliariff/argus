from .base import Base


class Ttfb(Base):
    def build(self):
        return {
            "measurement": self.measurement(),
            "tags": self.tags(),
            "time": self.time(),
            "fields": {
                "value": float(self.value)
            }
        }

    def is_valid(self):
        data = self.data['data']['average']['firstView']
        self.value = data.get('TTFB')
        return self.value != None

    def measurement(self):
        return 'ttfb'
