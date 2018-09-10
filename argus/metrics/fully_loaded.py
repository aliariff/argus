from .base import Base


class FullyLoaded(Base):
    def fill(self):
        return self.default_fill()

    def is_valid(self):
        return self.get_value_from_column("fullyLoaded") != None

    def measurement(self):
        return "fully_loaded"

    def fields(self):
        return {"value": float(self.get_value_from_column("fullyLoaded"))}
