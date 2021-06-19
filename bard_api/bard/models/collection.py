from bard.core import db
from bard.models.common import IdModel, DatedModel, make_textid, SoftDeleteModel
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB
import logging

log = logging.getLogger(__name__)


# class Collection(db.Model, IdModel, SoftDeleteModel):
#     label = db.Column(db.Unicode)
#     foreign_id = db.Column(db.Unicode, unique=True, nullable=False)
#
#     def touch(self):
#         self.updated_at = datetime.utcnow()
#         db.session.add(self)
#
#     def update(self, data):
#         self.label = data.get("label", self.label)
#         log.info("I GET CALLED AND SELF.LABEL IS {}".format(self.label))
#         self.touch()
#         db.session.flush()
#
#     @classmethod
#     def create(cls, data, created_at=None):
#         foreign_id = data.get("foreign_id") or make_textid()
#         collection = cls.by_foreign_id(foreign_id, deleted=True)
#         if collection is None:
#             collection = cls()
#             collection.created_at = created_at
#             collection.foreign_id = foreign_id
#         collection.update(data)
#         collection.deleted_at = None
#         return collection
#
#     def to_dict(self):
#         data = self.to_dict_dates()
#         data.update(
#             {
#                 "id": self.id,
#                 "collection_id": self.id,
#                 "foreign_id": self.foreign_id
#             }
#         )
#         return data
#
#     @classmethod
#     def by_foreign_id(cls, foreign_id, deleted=False):
#         if foreign_id is None:
#             return
#         q = cls.all(deleted=deleted)
#         return q.filter(cls.foreign_id == foreign_id).first()
#
#     def __repr__(self):
#         return '<Collection %r>' % self.label
#
#     def __str__(self):
#         return self.foreign_id
#
