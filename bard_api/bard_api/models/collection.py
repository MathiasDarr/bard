from bard_api.app import db
import logging

log = logging.getLogger(__name__)

class Collection(db.Model):
    label = db.Column(db.Unicode)

    def update(self, data):
        self.label = data.get("label", self.label)

    @classmethod
    def create(cls, data, created_at=None):
        collection = cls()
        return collection
