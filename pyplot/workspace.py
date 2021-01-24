from pystar.pyplot.GlobalSceneManager import GSM
from pystar.objs.dataset import DataSet, Data, MetaData, XYZPos, PlotType

from pystar.objs.workspace import Workspace

def workspace(wsID, name, description="", force_creation=False):
  workspace = Workspace(title=wsID, name=name, description=description)
  GSM.set_workspace(workspace)
  if force_creation:
    workspace.create()
  return workspace