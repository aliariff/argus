from .base import Base

class Ttff(Base):
  def measurement(self):
    'ttfb'

  def fields(self):
    self.data['mean']['TTFB_mean']
