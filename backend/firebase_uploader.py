import requests
import firebase_admin
from pathlib import Path
from collections import defaultdict
from firebase_admin import credentials, firestore

from pystar.objs.user import User
from pystar.objs.dataset import DataSet

class FireBaseUploader:
  _admin = None
  
  def __init__(self, user=User("GenericUser"), master_collection=u'users'):    
    self.master_collection = master_collection
    self.user = user
    cred = firebase_admin.credentials.Certificate(
      f"{Path.home()}/.pystar/keys/firebase.json"
    )
    try:
      app = firebase_admin.initialize_app(cred)
    except ValueError:
      pass

  
  @classmethod
  def admin(cls):
    if cls._admin is None:
      cls._admin = cls()
    return cls._admin

  def set_workspace(self, workspace):
    store = firebase_admin.firestore.client()
    usersRef = store.collection(self.master_collection)
    docRef = usersRef.document("GenericUser")
    workspaceRef = docRef.collection(u"workspaces")
    fxDocumentRef = workspaceRef.document(workspace.title)
    return fxDocumentRef.set({"name":workspace.name, "description":workspace.description})
    
  def upload(self, workspace, dataset):
    """
    A workspace represent one AR view, i.e., one workspace can have multiple datasets. 
    Raises RuntimeError if workspace does not exists. In this case call set_worksapce before calling
    this method.
    """
    store = firebase_admin.firestore.client()
    usersRef = store.collection(self.master_collection) # u'datasets'
    docRef = usersRef.document(self.user.username)
    workspaceRef = docRef.collection(u"workspaces")
    workspaceDocumentRef = workspaceRef.document(workspace.title)
    doc = workspaceDocumentRef.get()
    if not doc.exists:
      err = f"Workspace {workspace.name} does not exist. CAll set_workspace function before uploading data"
      raise RuntimeError(err)
    fxColRef = workspaceDocumentRef.collection("datasets")
    finalDocRef = fxColRef.document(dataset.title)

    finalDocRef.set(dataset.dict())
    print("Done Uploading", dataset.title, "to", workspace.title)

  def list_datasets(self, workspace):
    """
    A workspace represent one AR view, i.e., one workspace can have multiple datasets. 
    Raises RuntimeError if workspace does not exists. In this case call set_worksapce before calling
    this method.
    """
    store = firebase_admin.firestore.client()
    usersRef = store.collection(self.master_collection) # u'datasets'
    docRef = usersRef.document(self.user.username)
    workspaceRef = docRef.collection(u"workspaces")
    workspaceDocumentRef = workspaceRef.document(workspace.title)
    doc = workspaceDocumentRef.get()
    if not doc.exists:
      err = f"Workspace {workspace.name} does not exist. CAll set_workspace function before uploading data"
      raise RuntimeError(err)
    fxColRef = workspaceDocumentRef.collection("datasets")
    return [d.id for d in fxColRef.list_documents()]
    

  def delete_dataset_in_workspace(self, workspace, dataset):
    store = firebase_admin.firestore.client()
    usersRef = store.collection(self.master_collection) # u'datasets'
    docRef = usersRef.document(self.user.username)
    workspaceRef = docRef.collection(u"workspaces")
    workspaceDocumentRef = workspaceRef.document(workspace.title)
    doc = workspaceDocumentRef.get()
    if not doc.exists:
      err = f"Workspace {workspace.name} does not exist. Call set_workspace function before deleting data"
      raise RuntimeError(err)
    fxColRef = workspaceDocumentRef.collection("datasets")
    ds_name = dataset if isinstance(dataset, str) else dataset.title
    finalDocRef = fxColRef.document(ds_name)
    finalDocRef.delete()

  def workspace_exists(self, workspace):
    store = firebase_admin.firestore.client()
    usersRef = store.collection(self.master_collection) # u'datasets'
    docRef = usersRef.document(self.user.username)
    workspaceRef = docRef.collection(u"workspaces")
    workspaceDocumentRef = workspaceRef.document(workspace.title)
    doc = workspaceDocumentRef.get()
    return doc.exists

