
from .Model import Model
from datetime import datetime
from google.cloud import datastore

def from_datastore(entity):
    """
    Datastore returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        [ quote, author, source, date, added ]
    'quote', 'author', 'source', and 'date' are Python strings
    and 'added' is a Python datetime
    """
    if not entity:
        return []
    if isinstance(entity, list):
        entity = entity.pop()
    return [entity['quote'],entity['author'],entity['source'],entity['date'],entity['added']]

class model(Model):
    def __init__(self):
        self.client = datastore.Client('cloud-leon-marvleon')

    def select(self):
        query = self.client.query(kind = 'Quote')
        entities = list(map(from_datastore,query.fetch()))
        return entities

    def insert(self,quote,author,source,date):
        key = self.client.key('Quote')
        rev = datastore.Entity(key)
        rev.update( {
            'quote': quote,
            'author' : author,
            'source': source,
            'date' : date,
            'added' : datetime.today()
            })
        self.client.put(rev)
        return True