'''
it is the count of elements on your document (and any
 documents within iFrames). It's useful for getting an 
 idea for how complex the page is and should be really
  interesting to watch over time (and in aggregate).
'''

from .base import Base


class DomElements(Base):
    def fill(self):
        return {
            "measurement": self.measurement(),
            "tags": self.tags(),
            "time": self.time(),
            "fields": {
                "value": float(self.value)
            }
        }

    def is_valid(self):
        self.value = None
        data = self.data['data']['average']['firstView']
        if isinstance(data, dict):
            self.value = data.get('domElements')
        return self.value != None

    def measurement(self):
        return 'DOM_elements'
