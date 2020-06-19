from model.mapping import Base
import uuid

from sqlalchemy import Column, String, UniqueConstraint


class Sport(Base):
    __tablename__ = 'sports'

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(1096), nullable=True)

    def __repr__(self):
        return "<Sport %s>" % self.name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
