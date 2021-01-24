import gc
import numpy as np
from collections import OrderedDict


from pystar.pyplot.GlobalSceneManager import GSM

from pystar.pyplot.hollowAxis import HollowAxis, HollowAxisTypes
from pystar.pyplot.figs import Fig

from pystar.objs.dataset import DataSet, Data, MetaData, XYZPos, PlotType

class Reach:
  couch   = "couch"
  desk    = "desk"
  room    = "room"
  block   = "block"
  horizon = "horizon"


class SceneManager:
  num = 0
  figs = OrderedDict()
  data_ix = 0
  def __init__(self, data_list, metadatas, dataset_names=None):
    self.id = ""
    self.num = SceneManager.next_num()
  
    _ds_names = dataset_names if dataset_names is not None else self.sequencial_dsnames(len(data_list))
    self.datasets = [DataSet(n, d, m) for n,d,m in zip(_ds_names, data_list, metadatas) ]
    

  def next_data(self):
    ret = self.datasets[SceneManager.data_ix % len(self.datasets) ]
    SceneManager.data_ix += 1
    return ret

  @property
  def axs(self):
    return self.datasets

  @classmethod
  def next_num(cls):
    cls.num += 1
    return cls.num

  def sequencial_dsnames(self, N):
    return [f"DS{self.id}{i}" for i in range(1,N+1) ]

  def get_datasets(self):
    return self.datasets

  def destroy(self):
    pass

  def set_id(self, _id):
    self.id = str(_id)
    sequencial_dsnames = self.sequencial_dsnames(len(self.datasets))
    for ds, name in zip(self.datasets,sequencial_dsnames):
      ds.title = name
    




class CilinderScene(SceneManager):

  def __init__(self, figsize=None, rows=2, columns=4, radius=1, height=4, foot_height=0, ):
    padding = 0.01
    ZOOM = 16
    _figsize = (height/rows - padding*rows, height/rows - padding*rows, height/rows - padding*rows) if figsize is None else figsize
    _figsize = [s/ZOOM for s in _figsize]

    THETAS = [-np.pi/2 + 2*np.pi / columns * i for i in range(columns)]

    R = radius
    
    XYZs = [XYZPos(R*np.cos(theta)/ZOOM, H/ZOOM, R*np.sin(theta)/ZOOM)
            for theta in THETAS 
            for H in [height*i+foot_height for i in range(0,rows)] 
           ]
    
    
    metadatas = [
                  MetaData(title="", xlabel="X", ylabel="Y", 
                        plot_type= PlotType.ScatterPlot,
                        figsize=_figsize, 
                        plotScale=1,
                        xyzpos=xyz,
                        title_fontsize=0.2
                        )
                  for xyz in XYZs]

    super().__init__([Data() for _ in metadatas],metadatas)



class SingleScatter(SceneManager):

  def __init__(self, figsize, xyzpos=None):
    _figsize = (3,3,2) if figsize is None else figsize

    ZOOM = 32
    _xyz = XYZPos(xyzpos[0], xyzpos[1], xyzpos[2]) if xyzpos is not None else XYZPos(-1/ZOOM, -6/ZOOM, -8/ZOOM)
    metadata = MetaData(title="", xlabel="X", ylabel="Y", 
                        plot_type= PlotType.ScatterPlot,
                        figsize=_figsize, 
                        plotScale=1/ZOOM,
                        xyzpos=_xyz, 
                        title_fontsize=0.2
                      )

    super().__init__([Data()],[metadata])



def scene(layout_template, scene_size=None, *args, **kwargs):
  if layout_template == "simple":
    _S = SingleScatter(scene_size, *args, **kwargs)
  elif layout_template == "cilinder":
    _S = CilinderScene(scene_size, *args, **kwargs)
  GSM.set_active_scene(_S)
  return _S