"""
it is the count of elements on your document (and any
 documents within iFrames). It's useful for getting an
 idea for how complex the page is and should be really
  interesting to watch over time (and in aggregate).
"""

from .base import Base


class DomElements(Base):
    def fill(self):
        return self.default_fill()

    def is_valid(self):
        self.value = self.get_value_from_column("domElements")
        return self.value != None

    def measurement(self):
        return "DOM_elements"

    def fields(self):
        return {"value": float(self.value)}
