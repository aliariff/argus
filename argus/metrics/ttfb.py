from .base import Base


class Ttfb(Base):
    def measurement(self):
        return 'ttfb'

    def fields(self):
        return {
            "value": self.data['data']['average']['firstView']['TTFB']
        }
