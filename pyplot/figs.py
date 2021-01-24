import gc
from pystar.pyplot.scatter import scatter

class Fig:
  num = 0
  
  @classmethod
  def next_num(cls):
    cls.num += 1
    return cls.num

  def __init__(self, dataset):
    self.dataset = dataset
    self.num = Fig.next_num()

  def append(self, label, axis):
    self.dataset.append(label, axis)