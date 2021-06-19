import logging
from bard_api.app import db


from bard_api.models.collection import Collection

log = logging.getLogger(__name__)

def create_collection(data):
    collection = Collection.create(data)
    db.session.commit()
    return collection