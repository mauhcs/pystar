import numpy as np
from pystar.pyplot.GlobalSceneManager import GSM

from pystar.objs.dataset import Data, DataSet, MetaData, PlotType, XYZPos

from pystar.pyplot.hollowAxis import HollowAxis, HollowAxisTypes

def _mark_type(mark, size, color):
  if mark in ["box", "cube"]:
    return HollowAxisTypes.Box(size, color)
  elif mark in ["ball","o", "sphere"]:
    return HollowAxisTypes.Ball(size, color)
  else:
    return HollowAxisTypes.Box(size, color)

def safe(x):
  if isinstance(x, np.ndarray):
    return list(x)
  if not isinstance(x, list):
    return [x]
  return x

def scatter(x,y,z, color=None, mark=None, size=None, label=None, ax:HollowAxis=None):

  currentData = GSM.get_active_scene().next_data() if ax is None else ax

  _ax = _mark_type(mark, size, color)
  

  currentData.append(label, _ax.toAxis(safe(x),safe(y),safe(z) ))



  # fireManager.upload(workspace, dataset)