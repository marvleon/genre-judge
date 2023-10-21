# Marvin Leon cs430
# This file contains the constructor for the packackage when its imported by other python code.
# The constructor sets which model backend is going to be used for the site (sqlite3).
# The constructor instantiates the model from get_model() fucntion to return it to the web app.

model_backend = 'sqlite3'

if model_backend == 'sqlite3':
    from .model_sqlite3 import model

appmodel = model()

def get_model():
    return appmodel
