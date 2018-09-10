from .base import Base


class Ttfb(Base):
    def fill(self):
        return self.default_fill()

    def is_valid(self):
        return self.get_value_from_column("TTFB") != None

    def measurement(self):
        return "ttfb"

    def fields(self):
        return {"value": float(self.get_value_from_column("TTFB"))}
