from pystar.objs.dataset import Axis

from pystar.pyplot.arcolors import ARColor

class HollowAxis:
  def __init__(self, 
               dot_width, dot_height, dot_length, dot_corner_radius, 
               bumpable=False, dot_metalness=None, dot_roughness=None, color=None):
    
    self.color = color

    self.dot_width  = dot_width
    self.dot_height = dot_height
    self.dot_length = dot_length
    self.dot_corner_radius = dot_corner_radius 

    self.dot_metalness = dot_metalness
    self.dot_roughness = dot_roughness
    self.bumpable = bumpable

  def setColor(self, arcolor):
    if arcolor is None:
      return self
    if isinstance(arcolor,str):
      self.color = arcolor
      self.dot_metalness = 0.1
      self.dot_roughness = 0.5
    elif isinstance(arcolor, ARColor):
      self.color         = arcolor.name
      self.dot_metalness = arcolor.metal
      self.dot_roughness = arcolor.rough
    else:
      raise RuntimeError(f"ARColor:{arcolor} must be str|ARColor type")

    return self

  def toAxis(self, x, y, z):
    return Axis(x, y, z, self.dot_width, self.dot_height, self.dot_length, self.dot_corner_radius, 
               self.bumpable, self.dot_metalness, self.dot_roughness, self.color)

  @classmethod
  def makeHollow(self, ax):
    return HollowAxis(ax.dot_width, ax.dot_height, ax.dot_length, 
                      ax.dot_corner_radius, ax.bumpable, ax.dot_metalness, 
                      ax.dot_roughness, ax.color)


class BoxHollowAxis(HollowAxis):
  def __init__(self, size, color):
    _size = 0.1 if size is None else size
    super().__init__(dot_width=_size, dot_height=_size, dot_length=_size, dot_corner_radius=0)
    self.setColor(color)

class BallHollwoAxis(HollowAxis):
  def __init__(self, size, color):
    _size = 0.1 if size is None else size
    super().__init__(dot_width=_size, dot_height=_size, dot_length=_size, dot_corner_radius=_size)
    self.setColor(color)

class HollowAxisTypes:
  Box  = BoxHollowAxis
  Ball = BallHollwoAxis
