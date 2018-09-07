from .base import Base


class LoadTime(Base):
    def fill(self):
        return self.default_fill()

    def is_valid(self):
        self.value = self.get_value_from_column('loadTime')
        return self.value != None

    def measurement(self):
        return 'load_time'

    def fields(self):
        return {
            "value": float(self.value)
        }