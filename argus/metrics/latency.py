from .base import Base


class Latency(Base):
    def fill(self):
        return self.default_fill()

    def is_valid(self):
        return self.data["data"].get("latency") != None

    def measurement(self):
        return "latency"

    def fields(self):
        return {"value": float(self.data["data"].get("latency"))}
