import atexit
from collections import OrderedDict
import gc


class GSM: # 
  # Inspired by matplotlig Gcf: https://github.com/matplotlib/matplotlib/blob/master/lib/matplotlib/_pylab_helpers.py
  scenes = OrderedDict()
  activeWS = None # Active Workspace for plots

  @classmethod
  def destroy_all_scenes(cls):
    for manager in cls.scenes.values():
      manager.destroy()
    cls.scenes.clear()
    gc.collect(1)

  @classmethod
  def get_active_scene(cls):
    """Return the active manager, or *None* if there is no manager."""
    _S = next(reversed(cls.scenes.values())) if cls.scenes else None
    # print(_S, cls.scenes, cls.activeWS, f"ID:{id(cls)}")
    return _S
  
  @classmethod
  def get_scenes(cls):
    return reversed(cls.scenes.values()) if cls.scenes else None

  @classmethod
  def get_active_workspace(cls):
    return cls.activeWS

  @classmethod
  def set_active_scene(cls, manager):
    """Make *manager* the active manager."""
    cls.scenes[manager.num] = manager
    cls.scenes.move_to_end(manager.num)

  @classmethod
  def set_workspace(cls, workspace):
    
    if cls.activeWS is not None:
      if len(cls.scenes) > 0:
        print(f"Switching from Workspace with {len(cls.scenes)} existing Scenes. Scenes deleted.")
        cls.destroy_all_scenes()
    
    cls.activeWS = workspace
    # print("Setting Workspace:", cls.activeWS, GSM.activeWS, f"ID:{id(cls)}")
