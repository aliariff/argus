from .base import Base


class RenderStart(Base):
    def fill(self):
        return self.default_fill()

    def is_valid(self):
        self.value = self.get_value_from_column('render')
        return self.value != None

    def measurement(self):
        return 'render_start'

    def fields(self):
        return {
            "value": float(self.value)
        }
