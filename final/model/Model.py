# Marvin Leon cs430
# This file contains the abstract model class

#base class model
#select() and insert() methods will be overriden by sublasses for specific
#database implementations like in model_datastore.py
class Model():
    def select(self):
        # Gets all entries from DB return tuple containing all rows of database
        pass
    def insert(self, quote, author, source, date, added):
        pass
