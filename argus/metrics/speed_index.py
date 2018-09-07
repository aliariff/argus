from .base import Base


class SpeedIndex(Base):
    def fill(self):
        return self.default_fill()

    def is_valid(self):
        self.value = self.get_value_from_column("SpeedIndex")
        return self.value != None

    def measurement(self):
        return "speed_index"

    def fields(self):
        return {"value": float(self.value)}
