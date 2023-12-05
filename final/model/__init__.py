# Marvin Leon cs430
# This file contains the constructor for the packackage when its imported by other python code.
# The constructor sets which model backend is going to be used for the site (datastore).
# The constructor instantiates the model from get_model() fucntion to return it to the web app.

model_backend = "datastore"

if model_backend == "datastore":
    from .model_datastore import model

appmodel = model()

def get_model():
    return appmodel
