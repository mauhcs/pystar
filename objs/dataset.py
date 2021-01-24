class PlotType:
  SingleLine = "SingleLine"
  LinePlot   = "LinePlot" # multiline plots
  ScatterPlot = "ScatterPlot"

class XYZPos:
  def __init__(self,x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def list(self):
    return [self.x, self.y, self.z]

  def __str__(self):
    return f"XYZ({self.x, self.y, self.z}"
  
  def __repr__(self):
    return self.__str__()

class Axis:
  def __init__(self, x, y, z, 
               dot_width, dot_height, dot_length, dot_corner_radius, 
               bumpable=False, dot_metalness=None, dot_roughness=None, color=None):
    self.x = x
    self.y = y
    self.z = z
    self.color = color

    self.dot_width  = dot_width
    self.dot_height = dot_height
    self.dot_length = dot_length
    self.dot_corner_radius = dot_corner_radius 

    self.dot_metalness = dot_metalness
    self.dot_roughness = dot_roughness

    self.bumpable = bumpable

  def setColor(self, color_name, metal, rough):
    self.color         = color_name
    self.dot_metalness = metal
    self.dot_roughness = rough
    return self

  def dict(self):
    return {
      "x":[str(x) for x in self.x], 
      "y":[str(y) for y in self.y],
      "z":[str(z) for z in self.z],
      "color":self.color,
      "dotWidth":self.dot_width,
      "dotHeight":self.dot_height,
      "dotLength":self.dot_length,
      "dotCornerRadius":self.dot_corner_radius,
      "dotMetalness":self.dot_metalness,
      "dotRoughness":self.dot_roughness,
      "bumpable":self.bumpable,
      }


class EmptyAxis(Axis):
  def __init__(self,dot_width=None, dot_height=None, dot_length=None, dot_corner_radius=None, 
               bumpable=False, dot_metalness=None, dot_roughness=None, color=None):
               
    super().__init__([],[],[], 0.1, 0.1, 0.1, 0.1, bumpable, dot_metalness, dot_roughness, color)
  

class Data:
  def __init__(self, names=None, axis_list=None):
    self.names     = names if names is not None else []
    self.axis_list = axis_list if axis_list is not None else []

    self.ix = 0

  def append(self, name, ax):
    self.names.append(name)
    self.axis_list.append(ax)

  def maybe(self, name):
      if name is not None:
        return name
      else:
        self.ix += 1
        return f"AX{self.ix}"

  def dict(self):
    return {self.maybe(n):ax.dict() for n,ax in zip(self.names, self.axis_list)}


class MetaData:
  def __init__(self, title, xlabel, ylabel, plot_type, xyzpos, 
               figsize=(4.5, 4.5, 4.5), yrotation=0, plotScale=0.3, 
               title_fontsize=0.2, dot_size=0.08, dot_corner_radius=0.08):
    self.title             = title
    self.xlabel            = xlabel
    self.ylabel            = ylabel
    self.plot_type         = plot_type
    self.xyzpos            = xyzpos
    self.yrotation         = yrotation
    self.plotScale         = [plotScale for _ in range(3)]
    self.figsize           = figsize
    self.title_fontsize    = title_fontsize
    self.dot_size          = dot_size 
    self.dot_corner_radius = dot_corner_radius 

  def dict(self):
    return {
      "title":self.title,
      "xlabel":self.xlabel,
      "ylabel":self.ylabel,
      "plotType":self.plot_type, 
      "figsize":self.figsize, 
      "xyzpos":self.xyzpos.list(),
      "yrotation":self.yrotation,
      "plotScale":self.plotScale,
      "titleFontSize":self.title_fontsize,
      "dotSize":self.dot_size,
      "dotCornerRadius":self.dot_corner_radius
    }


class DataSet:

  def __init__(self, title, data, metadata):
    self.title    = title # firebase dataset ID
    self.data     = data
    self.metadata = metadata

  def append(self, name, ax):
    self.data.append(name, ax)

  def dict(self):
    return {
      "metadata":self.metadata.dict(),
      "data":self.data.dict()
      }
