from pystar.backend.firebase_uploader import FireBaseUploader

class Workspace:

  def __init__(self, title, name, description):
    self.title = title # workspace metadata in firebase
    self.name = name # displayed in the app
    self.description = description # displayed in the app

  def exists(self):
    FireBaseUploader.admin().workspace_exists(self)

  def create(self):
    FireBaseUploader.admin().set_workspace(self)

  def clean(self):
    admin = FireBaseUploader.admin()
    for ds_name in admin.list_datasets(self):
      admin.delete_dataset_in_workspace(self, ds_name)

    