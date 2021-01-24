from pystar.backend.firebase_uploader import FireBaseUploader

from pystar.pyplot.GlobalSceneManager import GSM

def design():
  WS = GSM.get_active_workspace()
  fireManager = FireBaseUploader()
  for S in GSM.get_scenes():  
    for ds in S.get_datasets():
      fireManager.upload(WS, ds)

  GSM.destroy_all_scenes()


  