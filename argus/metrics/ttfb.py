from .base import Base


class Ttfb(Base):
    def fill(self):
        return self.default_fill()

    def is_valid(self):
        self.value = self.get_value_from_column("TTFB")
        return self.value != None

    def measurement(self):
        return "ttfb"

    def fields(self):
        return {"value": float(self.value)}
